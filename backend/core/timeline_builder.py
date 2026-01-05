class TimelineBuilder:
    def build(self, logs):
        logs = sorted(logs, key=lambda x: x["timestamp"])
        return [
            {
                "time": log["timestamp"],
                "event": log["event"],
                "actor": log.get("user", "system"),
                "details": log.get("details", {})
            }
            for log in logs
        ]
