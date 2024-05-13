from fastapi import FastAPI, APIRouter, Query
from rag_service.app.rag import rag_chain

app = FastAPI()
router = APIRouter()

@router.get("/test", summary="Endpoint QA con RAG")
async def test_endpoint(parametro: str = Query(..., description="Consulta")):
    output = rag_chain.invoke(parametro)
    return {"input": parametro, "output": output}

app.include_router(router, prefix="/api")
