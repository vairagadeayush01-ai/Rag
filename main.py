"""
This is the main module of the application. It serves as the entry point for the program and contains the primary logic for initializing and running the application. The module may include functions, classes, and other components necessary for the application's functionality.
"""

from hr_assistant import config
from hr_assistant.logger import get_logger
from hr_assistant.pipeline import ask, build_hr_assistant

logger = get_logger(__name__)

def main():
    """
    The main function initializes the HR assistant and starts the interaction loop.
    It builds the HR assistant and continuously prompts the user for input until the user decides to exit.
    """
    logger.info("Starting command-line HR assistant")
    hr_assistant = build_hr_assistant(config.DATA_FILE_PATH)
    
    print("Welcome to the HR Assistant! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            logger.info("Command-line session ended by user")
            print("Exiting the HR Assistant. Goodbye!")
            break
        
        logger.info("Received command-line question")
        try:
            response = ask(hr_assistant, user_input)
        except Exception:
            logger.exception("Failed to answer command-line question")
            print("I couldn't complete that request right now.")
            continue
        print("="*60)
        print("user_input:", user_input)
        print("-"*60)
        print(f"HR Assistant: {response}")
        
if __name__ == "__main__":
    main()
