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

@app.get("/jobs")
def jobs():
    return [
        {
            "company": "Microsoft",
            "role": "Power BI Developer",
            "location": "Bangalore"
        },
        {
            "company": "Accenture",
            "role": "Data Analyst",
            "location": "Hyderabad"
        },
        {
            "company": "Deloitte",
            "role": "BI Developer",
            "location": "Chennai"
        }
    ]
