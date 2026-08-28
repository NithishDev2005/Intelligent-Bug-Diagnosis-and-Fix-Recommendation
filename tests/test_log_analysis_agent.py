from models.agent_models import BugReport
from agents.log_analysis_agent import LogAnalysisAgent


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)

agent = LogAnalysisAgent()

result = agent.analyze(bug)

print("\nLOG ANALYSIS RESULT")
print("=" * 40)
print("Failure Point:", result.failure_point)
print("Error Type:", result.error_type)
print("Key Error:", result.key_error_message)
print("Reasoning:", result.reasoning)