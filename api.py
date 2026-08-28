from fastapi import FastAPI, HTTPException

from models.agent_models import BugReport
from orchestrator.bug_diagnosis_orchestrator import BugDiagnosisOrchestrator


app = FastAPI(
    title="Smart Bug Analysis API",
    version="1.0.0",
    description="AI-powered bug diagnosis system",
)

orchestrator = BugDiagnosisOrchestrator()


@app.get("/")
def home():
    return {
        "message": "Smart Bug Analysis API is running"
    }


@app.post("/diagnose")
def diagnose_bug(bug: BugReport):
    try:
        result = orchestrator.diagnose(bug)
        return result.model_dump()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Bug diagnosis failed: {str(e)}"
        )