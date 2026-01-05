def has_excessive_privilege(event):
    return (
        event["event"] == "permission_granted"
        and event["details"].get("level") == "admin"
    )


def accessed_sensitive_data(event):
    return (
        event["event"] == "data_access"
        and event["details"].get("sensitive") is True
    )


def alert_ignored(event):
    return (
        event["event"] == "alert_triggered"
        and event["details"].get("action") == "ignored"
    )
