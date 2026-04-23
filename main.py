import os
from src.chunker import load_and_chunk
from src.embedding import create_db
from src.graph_flow import build_graph

PDF_PATH = "data/sample.pdf"

def setup():
    if not os.path.exists("chroma_db") or len(os.listdir("chroma_db")) == 0:
        print("Loading PDF...")
        chunks = load_and_chunk(PDF_PATH)

        print("Creating database...")
        create_db(chunks)

def chat():
    app = build_graph()

    print("PDF Chatbot Ready")
    print("Type exit to stop")

    while True:
        q = input("Ask: ")

        if q.lower() == "exit":
            break

        result = app.invoke({"query": q})
        print("\nAnswer:", result["answer"], "\n")

if __name__ == "__main__":
    setup()
    chat()