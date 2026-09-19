"""  build the agent that will use the tools to answer questions about the HR policy """

from langchain.agents import create_agent
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_hr_agent(llm,tools):
    """
    Create an HR agent that can answer questions about the HR policy using the provided language model and tools.

    Args:
        llm: The language model to be used by the agent.
        tools: A list of tools that the agent can use to retrieve information.
    Returns:
        An HR agent capable of answering questions about the HR policy. 
    """
    logger.info("Creating HR agent with %d tools", len(tools))
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT,
        debug=True,
    )
    logger.info("HR agent created successfully")
    return agent
