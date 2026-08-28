from models.agent_models import (
    BugReport,
    RootCauseResult,
)

from agents.remediation_agent import RemediationAgent


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)


root_cause = RootCauseResult(
    probable_root_cause=(
        "A required object or data reference is null "
        "before it is accessed."
    ),
    confidence="HIGH",
    supporting_bugs=["BUG-001"],
)


similar_bugs = [
    {
        "bug_id": "BUG-001",
        "document": "Historical bug",
        "metadata": {
            "severity": "HIGH",
            "priority": "P1",
            "resolution": "Added null validation.",
        },
    }
]


agent = RemediationAgent()

result = agent.analyze(
    bug=bug,
    root_cause=root_cause,
    similar_bugs=similar_bugs,
)


print("REMEDIATION RESULT")
print("=" * 50)
print("Recommended Fix:", result.recommended_fix)
print("Explanation:", result.explanation)
print("Preventive Action:", result.preventive_action)