import pandas as pd


REQUIRED_COLUMNS = [
    "bug_id",
    "title",
    "description",
    "error_type",
    "component",
    "root_cause",
    "resolution",
    "status",
    "technologies",
]


def validate_historical_bugs(bugs: pd.DataFrame) -> bool:
    """
    Validate the historical bug dataset.

    Returns:
        True if the dataset passes validation.
        Raises ValueError if validation fails.
    """

    # Check that all required columns exist
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in bugs.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check for missing values in required columns
    for column in REQUIRED_COLUMNS:
        if bugs[column].isnull().any():
            raise ValueError(
                f"Missing values found in column: {column}"
            )

    # Check for duplicate bug IDs
    if bugs["bug_id"].duplicated().any():
        raise ValueError("Duplicate bug IDs found.")

    # Check severity values
    valid_severities = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

    invalid_severities = set(bugs["severity"]) - valid_severities

    if invalid_severities:
        raise ValueError(
            f"Invalid severity values: {invalid_severities}"
        )

    # Check priority values
    valid_priorities = {"P0", "P1", "P2", "P3"}

    invalid_priorities = set(bugs["priority"]) - valid_priorities

    if invalid_priorities:
        raise ValueError(
            f"Invalid priority values: {invalid_priorities}"
        )

    return True