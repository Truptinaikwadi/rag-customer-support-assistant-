from typing import TypedDict
from langgraph.graph import StateGraph, END
from src.rag_pipeline import run_rag

class GraphState(TypedDict):
    query: str
    answer: str

def process_node(state):
    query = state["query"]
    answer = run_rag(query)
    return {"answer": answer}

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("process", process_node)

    graph.set_entry_point("process")
    graph.add_edge("process", END)

    return graph.compile()