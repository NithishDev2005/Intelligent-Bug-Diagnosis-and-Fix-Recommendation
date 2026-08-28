from models.agent_models import (
    BugReport,
    RootCauseResult,
    RemediationResult,
)


class RemediationAgent:
    """
    Recommends a fix based on the root cause
    and historical bug resolutions.
    """

    def analyze(
        self,
        bug: BugReport,
        root_cause: RootCauseResult,
        similar_bugs: list[dict],
    ) -> RemediationResult:

        historical_resolutions = []

        for historical_bug in similar_bugs:
            resolution = historical_bug.get("metadata", {}).get(
                "resolution"
            )

            if resolution:
                historical_resolutions.append(resolution)

        root_cause_text = root_cause.probable_root_cause.lower()

        if "null" in root_cause_text:
            recommended_fix = (
                "Add null validation before accessing the affected "
                "object and ensure the object is properly initialized."
            )

            preventive_action = (
                "Add null-safety checks, unit tests, and validation "
                "for the affected user profile flow."
            )

        elif "timeout" in root_cause_text:
            recommended_fix = (
                "Investigate the slow dependency and optimize the "
                "database or network operation causing the timeout."
            )

            preventive_action = (
                "Add timeout monitoring, performance testing, "
                "and appropriate retry mechanisms."
            )

        elif "authentication" in root_cause_text:
            recommended_fix = (
                "Validate authentication credentials or refresh the "
                "expired authentication token before making the request."
            )

            preventive_action = (
                "Implement token expiry handling and authentication "
                "failure monitoring."
            )

        else:
            recommended_fix = (
                "Investigate the identified failure point and apply "
                "a fix based on the root cause and historical evidence."
            )

            preventive_action = (
                "Add automated tests and monitoring around the "
                "affected functionality."
            )

        explanation = (
            f"The recommended fix addresses the identified root cause: "
            f"{root_cause.probable_root_cause}"
        )

        if historical_resolutions:
            explanation += (
                " Historical bug resolutions were also found and "
                "can be used as supporting guidance."
            )

        return RemediationResult(
            recommended_fix=recommended_fix,
            explanation=explanation,
            preventive_action=preventive_action,
        )