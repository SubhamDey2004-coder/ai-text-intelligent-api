from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Text Intelligence API",
    description="Production-level NLP API using Hugging Face",
    version="1.0.0"
)

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running successfully 🚀"}