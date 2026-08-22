# Read the raw data form the data file and return the content as a string

from langchain_community.document_loaders import TextLoader
from hr_assistant import config 

def load_document(file_path: str = config.DATA_FILE_PATH):
    """
    Load the document from the specified file path.

    Args:
        file_path (str): The path to the document file.

    Returns:
        str: The content of the document.
    """
    loader = TextLoader(file_path,encoding="utf-8")
    document = loader.load()
    return document

