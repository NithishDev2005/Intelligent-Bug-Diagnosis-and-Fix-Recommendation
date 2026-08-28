from pydantic import BaseModel, Field
from typing import Optional


class Bug(BaseModel):
    bug_id: str
    title: str
    description: str
    error_type: str
    stack_trace: Optional[str] = None
    severity: str
    priority: str
    component: str
    root_cause: str
    resolution: str
    status: str
    technologies: str