from ConcreteCrack.pipeline import DatIngestionTrainingPipeline
from ConcreteCrack import logger

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DatIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e: 
    logger.exception(e)
    raise e