from IOT_NIDS.constants import *
from IOT_NIDS.utils.common import read_yaml, create_directories,get_size 
from IOT_NIDS.entity.config_entity import DataIngestionConfig,EvaluationConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):

        # self.config = read_yaml(config_filepath)
        self.config = read_yaml(Path(__file__).resolve().parent / "config.yaml")
        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
           

        config = self.config.model_evaluation
        

        create_directories([config.root_dir])

        evaluation_config = EvaluationConfig(
            root_dir = config.root_dir,
            test_data_path = config.test_data_path,
            lables_data_path = config.lables_data_path,
            model_path = config.model_path,
            metric_file_name = config.metric_file_name,
            mlflow_uri="https://dagshub.com/RCgit123/IOT-Network-Intrusion-Detection-System.mlflow",
           
        )

        return evaluation_config