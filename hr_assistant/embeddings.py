# Generate embeddings for the document chunks

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embeddings_model():
    """
    Initialize and return the Jina embeddings model.

    Returns:
        JinaEmbeddings: The initialized embeddings model.
    """
    embeddings_model = JinaEmbeddings(model_name=config.EMBEDDINGS_MODEL_NAME)
    return embeddings_model
