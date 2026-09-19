# connect to the llm( brain of ht eassistant) and get the response

from langchain_groq import ChatGroq
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    """
    Initialize and return the ChatGroq language model.

    Returns:
        ChatGroq: The initialized language model.
    """
    logger.info("Initializing LLM: %s", config.LLM_MODEL_NAME)
    llm = ChatGroq(
        model=config.LLM_MODEL_NAME,
        api_key=config.GROQ_API_KEY,
        temperature=config.LLM_TEMPERATURE,
        # max_output_tokens=config.LLM_MAX_OUTPUT_TOKENS
    )
    logger.info("LLM initialized successfully")
    return llm
