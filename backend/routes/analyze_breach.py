from fastapi import APIRouter, HTTPException
from services.log_store import log_store
from core.timeline_builder import TimelineBuilder
from core.rule_engine import RuleEngine

router = APIRouter(prefix="/analysis", tags=["Analysis"])

@router.get("/breach")
def analyze():
    logs = log_store.get_all()
    if not logs:
        raise HTTPException(status_code=400, detail="No logs uploaded")

    timeline = TimelineBuilder().build(logs)
    report = RuleEngine().evaluate(timeline)

    return {
        "timeline": timeline,
        "failure_report": report
    }
