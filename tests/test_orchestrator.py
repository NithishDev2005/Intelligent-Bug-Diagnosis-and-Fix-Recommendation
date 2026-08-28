from models.agent_models import BugReport
from orchestrator.bug_diagnosis_orchestrator import BugDiagnosisOrchestrator


# Create a sample bug
bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)


# Create orchestrator
orchestrator = BugDiagnosisOrchestrator()


# Run complete diagnosis
result = orchestrator.diagnose(bug)


# Display final result
print("\n" + "=" * 60)
print("FINAL BUG DIAGNOSIS")
print("=" * 60)

print("Severity:", result.severity)
print("Priority:", result.priority)
print("Failure Point:", result.failure_point)
print("Error Type:", result.error_type)
print("Similar Bugs:", result.similar_bugs)
print("Root Cause:", result.probable_root_cause)
print("Confidence:", result.confidence)
print("Recommended Fix:", result.recommended_fix)
print("Preventive Action:", result.preventive_action)

print("=" * 60)