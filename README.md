# HR Policy Manager

This project is a simple Retrieval-Augmented Generation (RAG) prototype for working with HR policy documents. It is set up to load policy text, process it with LangChain, store embeddings in FAISS, and explore the workflow in a Jupyter notebook.

## Project Structure

- `rag.ipynb` - main notebook for experimenting with the RAG pipeline
- `data/hr_policy.txt` - source HR policy document used for retrieval
- `requirements.txt` - Python dependencies for the project
- `basicragenv/` - local virtual environment

## Requirements

- Python 3.10+
- A valid API key for the LLM provider you plan to use

## Installation

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your environment variables to `.env`.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

## How To Run

Start Jupyter Notebook and open `rag.ipynb`:

```bash
jupyter notebook
```

If you extend this into a UI, `streamlit` is already included in the dependencies for building a lightweight app interface.

## Purpose

The goal of this project is to make HR policy information easier to search and question through natural language, instead of manually reading long policy documents.
