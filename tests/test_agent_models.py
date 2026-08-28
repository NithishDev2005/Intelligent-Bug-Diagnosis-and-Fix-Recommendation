from models.agent_models import (
    BugReport,
    TriageResult,
    LogAnalysisResult,
)


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)

triage = TriageResult(
    severity="HIGH",
    priority="P1",
    reasoning="The application crashes during a core user operation.",
)

log_analysis = LogAnalysisResult(
    failure_point="UserService.getProfile",
    error_type="NullPointerException",
    key_error_message="UserProfile object is null",
    reasoning="The stack trace indicates a null object access.",
)

print("BugReport:", bug)
print("TriageResult:", triage)
print("LogAnalysisResult:", log_analysis)