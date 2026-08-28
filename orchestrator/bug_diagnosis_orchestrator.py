from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent
from agents.duplicate_detection_agent import DuplicateDetectionAgent
from agents.root_cause_agent import RootCauseAgent
from agents.remediation_agent import RemediationAgent
from rag.retriever import BugRetriever
from models.agent_models import BugDiagnosisResult


class BugDiagnosisOrchestrator:

    def __init__(self):
        self.triage_agent = TriageAgent()
        self.log_analysis_agent = LogAnalysisAgent()
        self.duplicate_agent = DuplicateDetectionAgent()
        self.root_cause_agent = RootCauseAgent()
        self.remediation_agent = RemediationAgent()
        self.retriever = BugRetriever()

    def diagnose(self, bug):
        try:
            # 1. Triage
            triage = self.triage_agent.analyze(bug)

            # 2. Log analysis
            log_analysis = self.log_analysis_agent.analyze(bug)

            # 3. Find similar historical bugs
            similar_bugs = self.retriever.retrieve(
                bug.description
            )

            # 4. Root cause
            root_cause = self.root_cause_agent.analyze(
                bug=bug,
                log_analysis=log_analysis,
                similar_bugs=similar_bugs,
            )

            # 5. Remediation
            remediation = self.remediation_agent.analyze(
                bug=bug,
                root_cause=root_cause,
                similar_bugs=similar_bugs,
            )

            # 6. Build final structured result
            return BugDiagnosisResult(
                severity=triage.severity,
                priority=triage.priority,
                failure_point=log_analysis.failure_point,
                error_type=log_analysis.error_type,
                similar_bugs=[
                    item["bug_id"] for item in similar_bugs
                ],
                probable_root_cause=root_cause.probable_root_cause,
                confidence=root_cause.confidence,
                recommended_fix=remediation.recommended_fix,
                preventive_action=remediation.preventive_action,
            )

        except Exception as e:
            print(f"Diagnosis pipeline error: {e}")
            raise