from src.retriever import get_retriever
from src.llm import ask_llm

def run_rag(question):
    retriever = get_retriever()

    docs = retriever.invoke(question)

    if not docs:
        return "No relevant information found."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Use the below context to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    return ask_llm(prompt)