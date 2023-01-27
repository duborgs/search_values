from fastapi import FastAPI


app = FastAPI(
    docs="/docs",
    redocs="/redoc",
    version="0.1.0",
    description="Projeto responsável por buscar cotações na internet",
    title="Search Values"
)

@app.get("/health_check")
async def health_check():
    return { "version": "0.1.0",
              "message":"Hi!"}