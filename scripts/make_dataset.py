"""Serialize the task dataset deterministically. 10 seeds x 4 tiers = 40 tasks."""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from dataclasses import asdict
from simulator import generate_scenario, TIERS

tasks = []
for tier in TIERS:
    for i in range(10):
        seed = 1000 * (TIERS.index(tier) + 1) + i
        sc = generate_scenario("market_data", tier, seed)
        d = asdict(sc)
        d["tier"] = tier
        d["task_id"] = f"x402gym-{tier}-{i:02d}"
        tasks.append(d)

out = os.path.join(os.path.dirname(__file__), "..", "tasks", "dataset.json")
with open(out, "w") as f:
    json.dump(tasks, f, indent=2)
print(f"wrote {len(tasks)} tasks -> {out}")
