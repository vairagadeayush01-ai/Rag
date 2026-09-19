import os
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

# build_vector_store

def build_vector_store(chunks):
    """
    Build a FAISS vector store from the provided document chunks.

    Args:
        chunks (list): A list of document chunks.
    Returns:
        FAISS: The constructed FAISS vector store.
    """
    logger.info("Building vector store from %d chunks", len(chunks))
    embeddings_model = get_embeddings_model()
    vector_store = FAISS.from_documents(chunks, embeddings_model)
    logger.info("Vector store built successfully")
    return vector_store

# save_vector_store

def save_vector_store(vector_store, path=config.VECTOR_STORE_PATH)->None:
    """
    Save the FAISS vector store to the specified path.

    Args:
        vector_store (FAISS): The FAISS vector store to be saved.
        path (str): The path where the vector store will be saved.
    """
    logger.info("Saving vector store to %s", path)
    vector_store.save_local(path)
    logger.info("Vector store saved successfully")

# load_vector_store

def load_vector_store(path=config.VECTOR_STORE_PATH):
    """
    Load the FAISS vector store from the specified path.

    Args:
        path (str): The path from where the vector store will be loaded.

    Returns:
        FAISS: The loaded FAISS vector store.
    """
    logger.info("Loading vector store from %s", path)
    embeddings_model = get_embeddings_model()
    vector_store = FAISS.load_local(
        path, embeddings_model, allow_dangerous_deserialization=True
    )
    logger.info("Vector store loaded successfully")
    return vector_store 

def vector_store_exists(path=config.VECTOR_STORE_PATH)->bool:
    """
    Check if the FAISS vector store exists at the specified path.

    Args:
        path (str): The path to check for the vector store.     

    Returns:
        bool: True if the vector store exists, False otherwise.
    """
    exists = os.path.exists(path)
    logger.info("Vector store path %s exists: %s", path, exists)
    return exists

def get_retriever(vector_store,k:int=config.TOP_K_RESULTS):
    """
    Get a retriever from the FAISS vector store.

    Args:
        vector_store (FAISS): The FAISS vector store.
        k (int): The number of top results to retrieve.

    Returns:
        Retriever: The retriever object for querying the vector store.
    """
    logger.info("Creating retriever with top_k=%d", k)
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    logger.info("Retriever created successfully")
    return retriever