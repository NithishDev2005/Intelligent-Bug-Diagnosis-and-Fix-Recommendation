from models.agent_models import BugReport

from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent
from agents.duplicate_detection_agent import DuplicateDetectionAgent
from agents.root_cause_agent import RootCauseAgent
from agents.remediation_agent import RemediationAgent


class BugDiagnosisPipeline:
    """
    Coordinates all bug analysis agents.
    """

    def __init__(self):
        self.triage_agent = TriageAgent()
        self.log_analysis_agent = LogAnalysisAgent()
        self.duplicate_agent = DuplicateDetectionAgent()
        self.root_cause_agent = RootCauseAgent()
        self.remediation_agent = RemediationAgent()

    def analyze(self, bug: BugReport) -> dict:
        """
        Run the complete bug diagnosis pipeline.
        """

        # 1. Triage
        triage = self.triage_agent.analyze(bug)

        # 2. Log analysis
        log_analysis = self.log_analysis_agent.analyze(bug)

        # 3. Find similar historical bugs
        similar_bugs = self.duplicate_agent.analyze(
            bug,
            n_results=3,
        )

        # 4. Determine root cause
        root_cause = self.root_cause_agent.analyze(
            bug=bug,
            log_analysis=log_analysis,
            similar_bugs=similar_bugs,
        )

        # 5. Recommend remediation
        remediation = self.remediation_agent.analyze(
            bug=bug,
            root_cause=root_cause,
            similar_bugs=similar_bugs,
        )

        return {
            "bug": bug,
            "triage": triage,
            "log_analysis": log_analysis,
            "similar_bugs": similar_bugs,
            "root_cause": root_cause,
            "remediation": remediation,
        }