RULES = {
    "architecture": {
        "max_raw": 28,
        "weight": 25,
    },
    "network": {
        "max_raw": 30,
        "weight": 25,
    },
    "identity": {
        "max_raw": 20,
        "weight": 15,
    },
    "assets": {
        "max_raw": 25,
        "weight": 15,
    },
    "monitoring": {
        "max_raw": 23,
        "weight": 20,
    },
}


def calculate_score(raw_scores: dict) -> dict:
    scores = {}

    for area, config in RULES.items():
        raw = raw_scores.get(area, 0)
        weighted = (raw / config["max_raw"]) * config["weight"]
        scores[area] = round(weighted, 2)

    total = round(sum(scores.values()), 2)

    return {
        "areas": scores,
        "total_score": total,
        "risk_level": get_risk_level(total),
    }


def get_risk_level(score: float) -> str:
    if score <= 20:
        return "Excellent"
    if score <= 40:
        return "Good"
    if score <= 60:
        return "Needs Improvement"
    if score <= 80:
        return "High Risk"
    return "Critical Risk"