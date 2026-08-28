from pydantic import BaseModel, Field


class BugReport(BaseModel):
    """
    Represents a new bug submitted by a developer.
    """

    title: str
    description: str
    error_type: str | None = None
    stack_trace: str | None = None
    component: str | None = None
    technologies: str | None = None


class TriageResult(BaseModel):
    """
    Output from the Triage Agent.
    """

    severity: str
    priority: str
    reasoning: str


class LogAnalysisResult(BaseModel):
    """
    Output from the Log Analysis Agent.
    """

    failure_point: str
    error_type: str
    key_error_message: str
    reasoning: str


class SimilarBug(BaseModel):
    """
    A historically similar bug retrieved from RAG.
    """

    bug_id: str
    similarity_context: str
    resolution: str


class RootCauseResult(BaseModel):
    """
    Output from the Root Cause Agent.
    """

    probable_root_cause: str
    confidence: str
    supporting_bugs: list[str]


class RemediationResult(BaseModel):
    """
    Output from the Remediation Agent.
    """

    recommended_fix: str
    explanation: str
    preventive_action: str