# chop the document into smaller chunks for better processing

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

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
    chunks = text_splitter.split_documents(documents)
    return chunks