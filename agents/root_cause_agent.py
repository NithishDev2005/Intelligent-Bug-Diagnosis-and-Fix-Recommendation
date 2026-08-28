from models.agent_models import RootCauseResult
from services.llm_service import LLMService


class RootCauseAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, bug, log_analysis, similar_bugs):
        prompt = f"""
You are an expert debugging engineer.

Bug:
{bug.title}

Description:
{bug.description}

Error:
{bug.error_type}

Stack Trace:
{bug.stack_trace}

Log Analysis:
Failure Point: {log_analysis.failure_point}
Error Type: {log_analysis.error_type}
Key Error: {log_analysis.key_error_message}

Historical Similar Bugs:
{similar_bugs}

Determine the most likely root cause.

Return ONLY:

ROOT_CAUSE: <clear root cause>
CONFIDENCE: HIGH, MEDIUM, or LOW
REASONING: <brief explanation>
"""

        response = self.llm.generate(prompt)

        root_cause = response
        confidence = "MEDIUM"
        reasoning = response

        for line in response.splitlines():
            line = line.strip()

            if line.upper().startswith("ROOT_CAUSE:"):
                root_cause = line.split(":", 1)[1].strip()

            elif line.upper().startswith("CONFIDENCE:"):
                confidence = line.split(":", 1)[1].strip().upper()

            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()

        if confidence not in {"HIGH", "MEDIUM", "LOW"}:
            confidence = "MEDIUM"

        return RootCauseResult(
            probable_root_cause=root_cause,
            confidence=confidence,
            reasoning=reasoning,
            supporting_bugs=[
    bug["bug_id"] for bug in similar_bugs
],
        )