"""
Langsmith tracing configuration.
"""

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def check_langsmith_tracing():
    """
    Check if Langsmith tracing is enabled and log the status.

    Returns:
        bool: True if tracing is enabled, False otherwise.
    """
    tracing_enabled = config.LANGSMITH_TRACING.lower() == "true"
    if tracing_enabled:
        logger.info("Langsmith tracing is enabled.")
        logger.info("Langsmith endpoint: %s", config.LANGSMITH_ENDPOINT)
        logger.info("Langsmith project: %s", config.LANGSMITH_PROJECT)
    else:
        logger.info("Langsmith tracing is disabled.plz set LANGSMITH_TRACING to 'true' in your environment variables to enable it.")
    
    return tracing_enabled