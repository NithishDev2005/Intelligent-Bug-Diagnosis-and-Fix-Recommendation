from utils.data_loader import (
    load_historical_bugs,
    load_historical_bug_models,
)

from utils.data_validator import validate_historical_bugs


# Load raw historical bug data
bugs = load_historical_bugs()

print("Total bugs:", len(bugs))

# Validate the raw data
validate_historical_bugs(bugs)

print("Data validation: PASSED")


# Convert rows into Bug models
bug_models = load_historical_bug_models()

print("Bug models created:", len(bug_models))


# Display the first Bug model
print("\nFirst Bug model:")
print(bug_models[0])