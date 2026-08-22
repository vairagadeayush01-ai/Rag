""" wires all th components together into one ready to use ageent
This is the single entry point for the HR assistant. It creates the
language model, tools, and agent, and returns a ready-to-use agent that can answer questions about the HR policy.
"""
from hr_assistant import config
from hr_assistant.agent import create_hr_agent
from hr_assistant.document_loader import load_document
from hr_assistant.llm import get_llm
from hr_assistant.splitter import split_into_chunks
from hr_assistant.tools import create_search_tool
from hr_assistant.vector_store import (
    build_vector_store,
    get_retriever,
    load_vector_store,
    save_vector_store,
    vector_store_exists,
)

def build_vector_store_for_documents(file_path : str=config.DATA_FILE_PATH):
    """
    Builds a vector store for the given documents. If the vector store already exists, it loads it from disk.
    Otherwise, it creates a new vector store and saves it to disk.

    Args:
        file_path (str): The path to the document file. Defaults to config.DATA_FILE_PATH.

    Returns:
        vector_store: The built vector store.
    """
    if vector_store_exists(config.VECTOR_STORE_PATH):
        print("Loading existing vector store...")
        vector_store = load_vector_store(config.VECTOR_STORE_PATH)
    else:
        print("Building new vector store...")
        documents = load_document(file_path)
        chunks = split_into_chunks(documents)
        vector_store = build_vector_store(chunks)
        save_vector_store(vector_store, config.VECTOR_STORE_PATH)
        print("vector store built and saved to disk.")

    return vector_store

def build_hr_assistant(file_path : str=config.DATA_FILE_PATH):
    """
    Builds the HR assistant agent.

    Args:
        file_path (str): The path to the document file. Defaults to config.DATA_FILE_PATH.

    Returns:
        agent: The built HR assistant agent.
    """
    vector_store = build_vector_store_for_documents(file_path)
    retriever = get_retriever(vector_store)
    llm = get_llm()
    search_tool = create_search_tool(retriever)
    agent = create_hr_agent(llm, [search_tool])
    return agent

def ask(agent,question : str)-> str:
    """
    Asks a question to the HR assistant agent and returns the answer.

    Args:
        agent: The HR assistant agent.
        question (str): The question to ask.
    
    Returns:
        str: The answer from the agent.
    """
    response=agent.invoke({"messages":[{"role":"user","content":question}]})
    return response["messages"][-1].content
