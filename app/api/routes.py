from fastapi import APIRouter
from ..models.query import QueryRequest
from ..core.llama import get_llama_index
from ..core.openai import get_openai_llm
from ..services.retriever import Retriever
from ..services.rag_engine import RAGEngine

router = APIRouter()

index = get_llama_index()
retriever = Retriever(index)
llm = get_openai_llm()
rag_engine = RAGEngine(retriever, llm)

@router.post("/rag/query")
def rag_query(request: QueryRequest):
    response = rag_engine.query(request.query)
    return {"response": response}
