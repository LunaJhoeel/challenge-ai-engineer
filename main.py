from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag_service.app.endpoints.qa import router as qa_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(qa_router, prefix='/qa', tags=["QA"])
