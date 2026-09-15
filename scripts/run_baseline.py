"""Run a scripted baseline policy over the dataset; print per-tier reward stats."""
import json, sys, os, statistics
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from simulator import Scenario, Endpoint, Episode
from rubric import grade
import policies

def load_tasks():
    p = os.path.join(os.path.dirname(__file__), "..", "tasks", "dataset.json")
    rows = json.load(open(p))
    out = []
    for d in rows:
        eps = [Endpoint(**e) for e in d.pop("endpoints")]
        tier = d.pop("tier"); task_id = d.pop("task_id")
        sc = Scenario(endpoints=eps, **d)
        out.append((task_id, tier, sc))
    return out

def run(policy_name):
    policy = getattr(policies, policy_name)
    by_tier = {}
    for task_id, tier, sc in load_tasks():
        ep = Episode(sc)
        policy(ep)
        g = grade(ep)
        by_tier.setdefault(tier, []).append(g["total"])
    return by_tier

if __name__ == "__main__":
    for pol in ["naive", "careful"]:
        res = run(pol)
        print(f"== policy: {pol} ==")
        for tier in ["easy", "medium", "hard", "very_hard"]:
            v = res[tier]
            print(f"  {tier:10s} mean={statistics.mean(v):.3f}  min={min(v):.3f}  max={max(v):.3f}")
