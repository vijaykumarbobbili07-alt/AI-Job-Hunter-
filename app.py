from fastapi import FastAPI
from jobs import get_jobs

app = FastAPI(
    title="AI Job Hunter",
    version="0.1"
)

@app.get("/")
def home():
    return {
        "project": "AI Job Hunter",
        "status": "Running",
        "developer": "Vijay"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/jobs")
def jobs():
    return get_jobs()
