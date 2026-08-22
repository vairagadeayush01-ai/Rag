# wrap the retriver as tool the agent can use to query the vector store
from langchain_core.tools import tool

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
        matching_chunks = retriever.invoke(question)
        return "\n\n".join(chunk.page_content for chunk in matching_chunks)
        
    return search_hr_policy
