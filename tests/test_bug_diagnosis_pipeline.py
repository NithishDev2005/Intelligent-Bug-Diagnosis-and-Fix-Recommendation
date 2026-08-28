from models.agent_models import BugReport
from agents.bug_diagnosis_pipeline import BugDiagnosisPipeline


bug = BugReport(
    title="NullPointerException in User Profile",
    description="Application crashes when opening a user profile.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    component="User Service",
    technologies="Java, Spring Boot",
)


pipeline = BugDiagnosisPipeline()

result = pipeline.analyze(bug)


print("\n" + "=" * 60)
print("SMART BUG DIAGNOSIS RESULT")
print("=" * 60)

print("\nTRIAGE")
print("Severity:", result["triage"].severity)
print("Priority:", result["triage"].priority)

print("\nLOG ANALYSIS")
print("Failure Point:", result["log_analysis"].failure_point)
print("Error Type:", result["log_analysis"].error_type)

print("\nSIMILAR HISTORICAL BUGS")

for bug in result["similar_bugs"]:
    print("-", bug["bug_id"])

print("\nROOT CAUSE")
print(result["root_cause"].probable_root_cause)
print("Confidence:", result["root_cause"].confidence)

print("\nRECOMMENDED FIX")
print(result["remediation"].recommended_fix)

print("\nPREVENTIVE ACTION")
print(result["remediation"].preventive_action)

print("\n" + "=" * 60)