# chop the document into smaller chunks for better processing

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def split_into_chunks(documents):
    """
    Split the documents into smaller chunks based on the specified chunk size and overlap.

    Args:
        documents (list): A list of documents to be split.

    Returns:
        list: A list of document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    logger.info("Splitting %d documents into chunks", len(documents))
    chunks = text_splitter.split_documents(documents)
    logger.info("Created %d document chunks", len(chunks))
    return chunks