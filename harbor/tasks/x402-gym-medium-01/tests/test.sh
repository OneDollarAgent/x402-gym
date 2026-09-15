#!/bin/bash
set -e
pip install -q pytest==8.4.1 pytest-json-ctrf==0.3.5
pytest --ctrf /logs/verifier/ctrf.json /tests/test_episode.py -rA || true
python3 - <<'EOF'
import json, os, pickle, sys
sys.path.insert(0, "/app/src")
from rubric import grade
try:
    with open("/app/state/episode.pkl", "rb") as f:
        ep = pickle.load(f)
    total = grade(ep)["total"]
except Exception:
    total = 0.0
threshold = float(os.environ.get("X402_PASS_THRESHOLD", "0.90"))
os.makedirs("/logs/verifier", exist_ok=True)
with open("/logs/verifier/reward.txt", "w") as f:
    f.write("1" if total >= threshold else "0")
print(f"total={total} threshold={threshold}")
EOF
