# Design & Build a RAG-Based Customer Support Assistant

A Retrieval-Augmented Generation (RAG) based PDF Question Answering System built using Python, LangChain, ChromaDB, LangGraph, and Groq API.

This project allows users to upload a PDF document, ask questions in natural language, and receive accurate answers based on the document content.



## Features

- PDF document ingestion
- Automatic text chunking
- Embedding generation
- Vector storage using ChromaDB
- Semantic search / retrieval
- LLM-powered contextual answers
- LangGraph workflow orchestration
- Human-in-the-Loop (HITL) ready architecture
- Reduces hallucination by using document context


## Tech Stack

- Python
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers
- Groq API
- PyPDF

## Project Structure

```text
rag-pdf-chatbot/
│── data/
│   └── sample.pdf
│── chroma_db/
│── src/
│   ├── chunker.py
│   ├── embedding.py
│   ├── retriever.py
│   ├── llm.py
│   ├── graph_flow.py
│   └── rag_pipeline.py
│── .env
│── main.py
│── requirements.txt
│── README.md
````


## How It Works

```text
PDF File
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB Storage
↓
User Query
↓
Retriever
↓
Groq LLM
↓
Final Answer
```
## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```


## Run Project

```bash
python main.py
```

---

## Example Queries

```text
What is refund policy?
Summarize this document.
What are payment terms?
When is support available?
```

## Use Cases

* Customer Support Assistant
* HR Policy Bot
* College Handbook Assistant
* Internal Company Knowledge Bot
* Product Manual Chatbot


## Challenges Solved

* API integration
* Vector search implementation
* PDF parsing
* Workflow routing
* Real-world debugging

## Future Improvements

* Streamlit Web UI
* Multi-PDF Support
* Chat Memory
* Voice Input
* Cloud Deployment
* Advanced HITL Escalation

## Author

Trupti Naikwadi

```
```
