import tensorflow as tf
from pathlib import Path
import os
import numpy as np
import mlflow
import mlflow.keras
import pandas as pd
from urllib.parse import urlparse
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import MinMaxScaler
from IOT_NIDS.entity.config_entity import EvaluationConfig
from IOT_NIDS.utils.common import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config=config

    def eval_metrics(self, actual, pred):    
        accuracy = accuracy_score(actual, pred)
        precision_per_class = precision_score(actual, pred, average=None)
        recall_per_class = recall_score(actual, pred, average=None)
        f1_score_per_class = f1_score(actual, pred, average=None)
        return accuracy, precision_per_class, recall_per_class, f1_score_per_class
    

    def log_into_mlflow(self):
        min_max_scaler = MinMaxScaler()
        x_test = pd.read_csv(self.config.test_data_path)
        y_test= pd.read_csv(self.config.lables_data_path)
        model = tf.keras.models.load_model(self.config.model_path)

       
        x_test = min_max_scaler.fit_transform(x_test)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_lable = model.predict(x_test)
            predicted_ids=np.argmax(predicted_lable, axis=1)

            (acc, pre, recal,f1sc) = self.eval_metrics(y_test, predicted_ids)
            
        
            # Saving metrics as local
            scores = {"acc": acc, "pre": pre.tolist(), "recl": recal.tolist(), "f1s": f1sc.tolist()}
            
            # for key, value in scores.items():
            #     if isinstance(value, np.ndarray):
            #         scores[key] = value.tolist()

            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_metric("accuracy", np.mean(acc))
            mlflow.log_metric("precision", np.mean(pre))
            mlflow.log_metric("recall", np.mean(recal))
            mlflow.log_metric("f1_score", np.mean(f1sc))
 # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="GRUModel")
            else:
                mlflow.sklearn.log_model(model, "model")

    
 