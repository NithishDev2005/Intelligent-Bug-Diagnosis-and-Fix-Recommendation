from models.agent_models import TriageResult
from services.llm_service import LLMService


class TriageAgent:
    """
    Uses the local LLM to determine bug severity and priority.
    """

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, bug):
        prompt = f"""
You are a software bug triage expert.

Analyze the following bug:

Title: {bug.title}
Description: {bug.description}
Error Type: {bug.error_type}
Stack Trace: {bug.stack_trace}
Component: {bug.component}
Technologies: {bug.technologies}

Determine:
1. Severity: LOW, MEDIUM, HIGH, or CRITICAL
2. Priority: P1, P2, P3, or P4
3. Brief reasoning

Return ONLY in this format:

SEVERITY: <value>
PRIORITY: <value>
REASONING: <one or two sentences>
"""

        response = self.llm.generate(prompt)

        severity = "MEDIUM"
        priority = "P2"
        reasoning = response

        for line in response.splitlines():
            line = line.strip()

            if line.upper().startswith("SEVERITY:"):
                severity = line.split(":", 1)[1].strip().upper()

            elif line.upper().startswith("PRIORITY:"):
                priority = line.split(":", 1)[1].strip().upper()

            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()

        valid_severities = {
            "LOW", "MEDIUM", "HIGH", "CRITICAL"
        }

        valid_priorities = {
            "P1", "P2", "P3", "P4"
        }

        if severity not in valid_severities:
            severity = "MEDIUM"

        if priority not in valid_priorities:
            priority = "P2"

        return TriageResult(
            severity=severity,
            priority=priority,
            reasoning=reasoning,
        )