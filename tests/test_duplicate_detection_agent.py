from models.agent_models import BugReport
from agents.duplicate_detection_agent import DuplicateDetectionAgent


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)


agent = DuplicateDetectionAgent()

results = agent.analyze(bug, n_results=3)

print("DUPLICATE DETECTION RESULT")
print("=" * 50)

print("Similar bugs found:", len(results))

for result in results:
    print("\nBug ID:", result["bug_id"])
    print("Severity:", result["metadata"]["severity"])
    print("Priority:", result["metadata"]["priority"])