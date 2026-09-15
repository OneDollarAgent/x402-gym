"""In-container CLI for x402-gym Harbor tasks.

Usage: python3 /app/harness.py <action> ['<json-args>']
State persists in $X402_STATE (default /app/state); every call appends to
trajectory.jsonl and prints the observation as JSON.
"""
import json, os, pickle, sys

sys.path.insert(0, os.environ.get("X402_SRC", "/app/src"))
from simulator import Scenario, Endpoint, Episode  # noqa: E402

STATE = os.environ.get("X402_STATE", "/app/state")
EP_PKL = os.path.join(STATE, "episode.pkl")
TRAJ = os.path.join(STATE, "trajectory.jsonl")
CONF = os.environ.get("X402_CONF", "/app/scenario.json")


def load_ep():
    if os.path.exists(EP_PKL):
        with open(EP_PKL, "rb") as f:
            return pickle.load(f)
    d = json.load(open(CONF))
    eps = [Endpoint(**e) for e in d.pop("endpoints")]
    for k in ("tier", "task_id"):
        d.pop(k, None)
    return Episode(Scenario(endpoints=eps, **d))


def main():
    os.makedirs(STATE, exist_ok=True)
    action = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    ep = load_ep()
    table = {
        "browse": lambda: {"services": ep.browse(),
                           "budget_remaining": ep.sc.budget - ep.spent},
        "request": lambda: ep.request(args.get("url", "")),
        "verify_registry": lambda: ep.verify_registry(args.get("address", "")),
        "pay": lambda: ep.pay(args.get("challenge_id", "")),
        "sign_siwe": lambda: ep.sign_siwe(args.get("message", "")),
        "flag_endpoint": lambda: ep.flag_endpoint(args.get("url", ""),
                                                  args.get("reason", "")),
        "answer": lambda: ep.answer(args.get("value"),
                                    args.get("evidence_ids", [])),
    }
    if action not in table:
        print(json.dumps({"error": f"unknown action {action!r}"}))
        sys.exit(2)
    out = table[action]()
    if action == "pay" and isinstance(out, dict):
        out["budget_remaining"] = ep.sc.budget - ep.spent
    with open(TRAJ, "a") as f:
        f.write(json.dumps({"action": action, "args": args,
                            "observation": out}, default=str) + "\n")
    with open(EP_PKL, "wb") as f:
        pickle.dump(ep, f)
    print(json.dumps(out, default=str))


if __name__ == "__main__":
    main()
