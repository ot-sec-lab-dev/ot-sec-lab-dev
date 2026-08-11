import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scoring import calculate_score


result = calculate_score({
    "architecture": 28,
    "network": 30,
    "identity": 20,
    "assets": 25,
    "monitoring": 23,
})

assert result["total_score"] == 100.0
assert result["risk_level"] == "Critical Risk"

print("TEST PASSED")