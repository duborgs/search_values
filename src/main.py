# main.py
import uvicorn
from fastapi import FastAPI

from src.search_values.core import settings

app = FastAPI(
    docs="/docs",
    redocs="/redoc",
    version="0.1.0",
    description="Projeto responsável por buscar cotações na internet",
    title="Search Values"
)

if __name__ == "__main__":
    uvicorn.run("routes:app",
                host=settings.HOST,
                port=settings.PORT,
                reload="true",
                )


