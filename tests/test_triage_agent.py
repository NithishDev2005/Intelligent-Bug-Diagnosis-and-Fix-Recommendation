from models.agent_models import BugReport
from agents.triage_agent import TriageAgent


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)

agent = TriageAgent()

result = agent.analyze(bug)

print("\nTRIAGE RESULT")
print("=" * 40)
print("Severity:", result.severity)
print("Priority:", result.priority)
print("Reasoning:", result.reasoning)