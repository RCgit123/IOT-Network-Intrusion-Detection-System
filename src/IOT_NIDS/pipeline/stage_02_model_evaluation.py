from IOT_NIDS.config.configuration import ConfigurationManager
from IOT_NIDS.components.model_evaluation import Evaluation
from IOT_NIDS import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation_config = Evaluation(config=model_evaluation_config)
        #model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

