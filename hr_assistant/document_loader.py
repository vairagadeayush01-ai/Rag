# Read the raw data form the data file and return the content as a string

from langchain_community.document_loaders import TextLoader
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def load_document(file_path: str = config.DATA_FILE_PATH):
    """
    Load the document from the specified file path.

    Args:
        file_path (str): The path to the document file.

    Returns:
        str: The content of the document.
    """
    logger.info(f"Loading document from {file_path}")

    try:
        loader = TextLoader(file_path, encoding="utf-8")
        document = loader.load()
    except Exception:
        logger.exception("Failed to load document from %s", file_path)
        raise

    logger.info("Loaded %d documents successfully", len(document))
    return document

