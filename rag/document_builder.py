from models.bug import Bug


def bug_to_document(bug: Bug) -> str:
    """
    Convert a Bug model into a searchable text document.
    """

    document = f"""
BUG ID: {bug.bug_id}

Title:
{bug.title}

Description:
{bug.description}

Error Type:
{bug.error_type}

Stack Trace:
{bug.stack_trace or "Not available"}

Component:
{bug.component}

Severity:
{bug.severity}

Priority:
{bug.priority}

Root Cause:
{bug.root_cause}

Resolution:
{bug.resolution}

Status:
{bug.status}

Technologies:
{bug.technologies}
""".strip()

    return document

def bug_to_metadata(bug: Bug) -> dict:
    """
    Extract structured metadata from a Bug model.
    """

    return {
        "bug_id": bug.bug_id,
        "severity": bug.severity,
        "priority": bug.priority,
        "component": bug.component,
        "status": bug.status,
        "technologies": bug.technologies,
    }