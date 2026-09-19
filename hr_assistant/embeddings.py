# Generate embeddings for the document chunks

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_embeddings_model():
    """
    Initialize and return the Jina embeddings model.

    Returns:
        JinaEmbeddings: The initialized embeddings model.
    """
    logger.info("Initializing embeddings model: %s", config.EMBEDDINGS_MODEL_NAME)
    embeddings_model = JinaEmbeddings(model_name=config.EMBEDDINGS_MODEL_NAME)
    logger.info("Embeddings model initialized")
    return embeddings_model
