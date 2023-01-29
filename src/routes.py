from main import app
from fastapi import APIRouter



@app.get("/health_check")
async def health_check():
    return { "version": "0.1.0",
              "message":"Hi!"}