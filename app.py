from fastapi import FastAPI

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
