import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scoring import calculate_score


def evaluate_assessment(raw_scores: dict) -> dict:
    result = calculate_score(raw_scores)

    return {
        "risk_score": result["total_score"],
        "risk_level": result["risk_level"],
        "areas": result["areas"],
    }