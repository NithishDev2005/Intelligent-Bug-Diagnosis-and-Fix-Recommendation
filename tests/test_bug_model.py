from models.bug import Bug


bug = Bug(
    bug_id="BUG-TEST-001",
    title="Test NullPointerException",
    description="Application crashes during profile loading.",
    error_type="NullPointerException",
    stack_trace="UserService.getProfile(UserService.java:142)",
    severity="HIGH",
    priority="P1",
    component="User Service",
    root_cause="Profile object is null.",
    resolution="Added null validation.",
    status="RESOLVED",
    technologies="Java,Spring Boot",
)


print("Bug model created successfully!")
print(bug)