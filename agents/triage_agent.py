from models.agent_models import TriageResult
from services.llm_service import LLMService


class TriageAgent:
    """
    Uses the local LLM for triage reasoning while applying
    deterministic rules for consistent severity and priority.
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

Determine the likely severity and priority.

Severity:
LOW, MEDIUM, HIGH, or CRITICAL

Priority:
P1, P2, P3, or P4

Return ONLY:

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
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL",
        }

        valid_priorities = {
            "P1",
            "P2",
            "P3",
            "P4",
        }

        if severity not in valid_severities:
            severity = "MEDIUM"

        if priority not in valid_priorities:
            priority = "P2"

        # -------------------------------------------------
        # Deterministic rules for serious application errors
        # -------------------------------------------------

        error_type = (bug.error_type or "").lower()
        description = (bug.description or "").lower()
        title = (bug.title or "").lower()

        crash_indicators = [
            "nullpointerexception",
            "application crashes",
            "application crash",
            "system crash",
            "fatal error",
            "unhandled exception",
        ]

        is_serious_crash = any(
            indicator in error_type
            or indicator in description
            or indicator in title
            for indicator in crash_indicators
        )

        if is_serious_crash:
            severity = "HIGH"
            priority = "P1"

        return TriageResult(
            severity=severity,
            priority=priority,
            reasoning=reasoning,
        )