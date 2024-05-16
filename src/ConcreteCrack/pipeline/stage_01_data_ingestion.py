from ConcreteCrack.config import ConfigurationManager
from ConcreteCrack.components import DataIngestion
from ConcreteCrack import logger




class DatIngestionTrainingPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
        
