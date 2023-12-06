from IOT_NIDS.constants import *
from IOT_NIDS.utils.common import read_yaml, create_directories,get_size 
from IOT_NIDS.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = Path(CONFIG_FILE_PATH),
        params_filepath = Path(PARAMS_FILE_PATH)):

        # self.config = read_yaml(config_filepath)
        self.config = read_yaml(Path(__file__).resolve().parent / "config.yaml")

        self.params = read_yaml(params_filepath)

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
    