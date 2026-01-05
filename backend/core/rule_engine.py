class RuleEngine:
    def evaluate(self, timeline):
        findings = []

        for event in timeline:
            if event["event"] == "permission_granted" and \
               event["details"].get("level") == "admin":
                findings.append(self._failure(
                    "Excessive Privilege",
                    "Admin rights granted without justification",
                    event
                ))

            if event["event"] == "alert_triggered" and \
               event["details"].get("action") == "ignored":
                findings.append(self._failure(
                    "Ignored Alert",
                    "Security alert not acted upon",
                    event
                ))

        return {
            "root_causes": findings,
            "preventive_rule": "Enforce least privilege & mandatory alert acknowledgment"
        }

    def _failure(self, title, description, event):
        return {
            "title": title,
            "description": description,
            "time": event["time"],
            "decision_failure": True
        }
