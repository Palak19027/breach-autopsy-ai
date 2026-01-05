from ai.insight_generator import generate_insights
from ai.explanation_formatter import format_explanation

# Test Case 1: Classic breach scenario
timeline = {
    "events": [
        {"type": "login", "time": "10:00"},
        {"type": "permission_granted", "level": "admin", "time": "10:01"},
        {"type": "alert_triggered", "severity": "high", "time": "10:05"},
        {"type": "no_response", "duration": "2 hours"},
        {"type": "data_accessed", "resource": "customer_db"}
    ],
    "flags": ["over_permission", "ignored_alert", "delayed_response"]
}

raw = generate_insights(timeline)
final = format_explanation(raw)

print("\n===== TEST RESULT =====\n")
for k, v in final.items():
    print(f"{k.upper()}: {v}")
