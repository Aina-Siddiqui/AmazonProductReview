from reviewClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from reviewClassifier.logging import logger

STAGE_NAME="DATA INGESTION STAGE"
try:
    logger.info(f">>> Starting {STAGE_NAME } >>>")
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"{STAGE_NAME} completed successfully")
except Exception as e:
    raise e