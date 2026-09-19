"""Streamlit UI for the HR Policy Assistant."""

import streamlit as st

from hr_assistant import config
from hr_assistant.logger import get_logger
from hr_assistant.pipeline import ask, build_hr_assistant

logger = get_logger(__name__)


st.set_page_config(
    page_title="HR Policy Assistant",
    layout="centered",
)


@st.cache_resource
def load_assistant():
    """Build and cache the HR assistant instance."""
    logger.info("Loading cached HR assistant")
    config.check_api_keys()
    assistant = build_hr_assistant(config.DATA_FILE_PATH)
    logger.info("Cached HR assistant loaded")
    return assistant


def reset_chat() -> None:
    """Clear the current chat history."""
    logger.info("Chat history cleared")
    st.session_state.messages = []


def main() -> None:
    """Render the Streamlit app."""
    logger.info("Rendering Streamlit application")
    st.title("HR Policy Assistant")
    st.caption("Ask questions about your HR policies and get answers from the policy document.")

    with st.sidebar:
        st.subheader("About")
        st.write("This app searches the HR policy knowledge base and answers employee questions.")
        st.button("Clear chat", on_click=reset_chat, use_container_width=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! Ask me anything about the HR policy.",
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask an HR policy question")
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Checking the HR policy..."):
            try:
                assistant = load_assistant()
                response = ask(assistant, prompt)
            except Exception as exc:
                logger.exception("Failed to answer Streamlit question")
                response = (
                    "I couldn't complete that request right now.\n\n"
                    f"Error: `{exc}`"
                )
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
