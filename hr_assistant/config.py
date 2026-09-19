import os
from dotenv import load_dotenv
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

load_dotenv()

# Tracing 
LANGSMITH_TRACING=os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT=os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY=os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT=os.getenv("LANGSMITH_PROJECT")

# Env variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

# define path
DATA_FILE_PATH = os.path.join("data", "hr_policy.txt")

# vector stores

# CLOUD MENORY\
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

# Models
LLM_MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDINGS_MODEL_NAME = "jina-embeddings-v2-base-en"

# CHUNK/TEXT SPLITTING
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# RETERIVALS RESULTS
LLM_TEMPERATURE=0.4
LLM_MAX_OUTPUT_TOKENS=1024
TOP_K_RESULTS = 3

# SYSTEM PROMPT
SYSTEM_PROMPT = """You are a helpful HR assistant. You have access to the company's HR policies and guidelines.
Your task is to provide accurate and concise answers to employee queries based on the information available in the
HR policies. If the information is not available, politely inform the employee that you do not have the answer."""

def check_api_keys()-> None:
    logger.info("Checking required API keys")
    if not GROQ_API_KEY:
        logger.error("GROQ_API_KEY is not set")
        raise ValueError("GROQ_API_KEY is not set. Please set it in your environment variables.")
    if not JINA_API_KEY:
        logger.error("JINA_API_KEY is not set")
        raise ValueError("JINA_API_KEY is not set. Please set it in your environment variables.")
    logger.info("Required API keys are available")
