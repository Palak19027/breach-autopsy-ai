def format_explanation(raw_text: str) -> dict:
    """
    Converts raw AI text into clean JSON.
    """
    result = {
        "root_cause": "",
        "ignored_signal": "",
        "wrong_decision": "",
        "preventive_rule": ""
    }

    lines = raw_text.split("\n")

    for line in lines:
        if line.startswith("Root Cause:"):
            result["root_cause"] = line.replace("Root Cause:", "").strip()
        elif line.startswith("Ignored Signal:"):
            result["ignored_signal"] = line.replace("Ignored Signal:", "").strip()
        elif line.startswith("Wrong Decision:"):
            result["wrong_decision"] = line.replace("Wrong Decision:", "").strip()
        elif line.startswith("Preventive Rule:"):
            result["preventive_rule"] = line.replace("Preventive Rule:", "").strip()

    return result
