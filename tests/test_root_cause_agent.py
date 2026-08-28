from models.agent_models import (
    BugReport,
    LogAnalysisResult,
)

from agents.root_cause_agent import RootCauseAgent


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)


log_analysis = LogAnalysisResult(
    failure_point="UserService.getProfile(UserService.java:142)",
    error_type="NullPointerException",
    key_error_message="Application crashes when opening a user profile.",
    reasoning="The stack trace indicates a null object access.",
)


similar_bugs = [
    {
        "bug_id": "BUG-001",
        "document": "Historical NullPointerException bug",
        "metadata": {
            "severity": "HIGH",
            "priority": "P1",
        },
    }
]


agent = RootCauseAgent()

result = agent.analyze(
    bug=bug,
    log_analysis=log_analysis,
    similar_bugs=similar_bugs,
)


print("ROOT CAUSE RESULT")
print("=" * 50)
print("Root Cause:", result.probable_root_cause)
print("Confidence:", result.confidence)
print("Supporting Bugs:", result.supporting_bugs)