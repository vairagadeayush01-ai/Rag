# wrap the retriver as tool the agent can use to query the vector store
from langchain_core.tools import tool
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_search_tool(retriever):
    """
    Create a search tool for querying the HR policy vector store.

    """
    @tool
    def search_hr_policy(question : str) -> str :
        """
        Search the HR policy vector store for relevant information based on the provided question.

        Args:
            question (str): The question to search for in the HR policy.
            
        Returns:
            str: The relevant information retrieved from the HR policy vector store.
        """
        logger.info("Searching HR policy for question: %s", question)
        try:
            matching_chunks = retriever.invoke(question)
        except Exception:
            logger.exception("HR policy search failed")
            raise
        logger.info("Retrieved %d matching chunks", len(matching_chunks))
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)
        
    return search_hr_policy
