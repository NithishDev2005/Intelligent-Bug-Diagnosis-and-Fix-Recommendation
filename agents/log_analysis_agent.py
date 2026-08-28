from models.agent_models import LogAnalysisResult
from services.llm_service import LLMService


class LogAnalysisAgent:
    """
    Uses the local LLM to analyze stack traces and identify
    the failure point and key error information.
    """

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, bug):
        prompt = f"""
You are an expert software debugging engineer.

Analyze this bug:

Title: {bug.title}
Description: {bug.description}
Error Type: {bug.error_type}
Stack Trace: {bug.stack_trace}
Component: {bug.component}
Technologies: {bug.technologies}

Identify:
1. The most likely failure point
2. The error type
3. The key error message
4. Brief reasoning

Return ONLY this format:

FAILURE_POINT: <value>
ERROR_TYPE: <value>
KEY_ERROR_MESSAGE: <value>
REASONING: <one or two sentences>
"""

        response = self.llm.generate(prompt)

        failure_point = "Unknown"
        error_type = bug.error_type
        key_error_message = "Unknown"
        reasoning = response

        for line in response.splitlines():
            line = line.strip()

            if line.upper().startswith("FAILURE_POINT:"):
                failure_point = line.split(":", 1)[1].strip()

            elif line.upper().startswith("ERROR_TYPE:"):
                error_type = line.split(":", 1)[1].strip()

            elif line.upper().startswith("KEY_ERROR_MESSAGE:"):
                key_error_message = line.split(":", 1)[1].strip()

            elif line.upper().startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()

        return LogAnalysisResult(
            failure_point=failure_point,
            error_type=error_type,
            key_error_message=key_error_message,
            reasoning=reasoning,
        )