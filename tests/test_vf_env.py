import json, os, sys, asyncio, importlib.util
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

pytestmark = pytest.mark.skipif(
    importlib.util.find_spec("verifiers") is None, reason="verifiers not installed")

from types import SimpleNamespace as Msg

def _run(coro):
    import asyncio
    return asyncio.run(coro)


def drive(env, state, actions):
    """Feed scripted JSON actions through env_response like a model would."""
    messages = []
    obs = None
    for act in actions:
        messages.append(Msg(role="assistant", content=json.dumps(act)))
        obs = _run(
            env.env_response(messages, state))
        if state["episode"].done:
            break
    return obs

def make_state(env, i=0):
    row = env.get_dataset()[i]
    return env.setup_state({"info": row["info"], "task": row["task"]})

def test_env_loads_all_tiers():
    import x402_gym
    for tier in ["easy", "medium", "hard", "very_hard"]:
        env = x402_gym.load_environment(tier=tier)
        assert len(env.get_dataset()) == 10

def test_full_rollout_careful_path():
    import x402_gym
    env = x402_gym.load_environment(tier="easy", num_examples=1)
    state = make_state(env)
    ep = state["episode"]
    adverts = ep.browse(); ep.turns = 0; ep.log.clear()  # peek for scripting
    paid_url = None
    for ad in adverts:
        if ad["scheme"] == "x402" and ad["price"] >= 300:
            paid_url = ad["url"]
    messages = [Msg(role="assistant", content=json.dumps({"action":"browse"}))]
    obs = _run(env.env_response(messages, state))
    services = json.loads(obs[0]["content"])["services"]
    targets = [s for s in services if s["scheme"] == "x402"]
    # verify + pay the honest (higher-priced, registry-listed) one
    for t in sorted(targets, key=lambda s: -s["price"]):
        r = _run(env.env_response(
            messages + [Msg(role="assistant", content=json.dumps({"action":"request","url":t["url"]}))], state))
        body = json.loads(r[0]["content"])
        if body.get("status") != 402: continue
        ch = body["challenge"]
        _run(env.env_response(
            messages + [Msg(role="assistant", content=json.dumps({"action":"verify_registry","address":ch["pay_to"]}))], state))
        rec = _run(env.env_response(
            messages + [Msg(role="assistant", content=json.dumps({"action":"pay","challenge_id":ch["challenge_id"]}))], state))
        body = json.loads(rec[0]["content"])
        if body.get("data"):
            val = next(iter(body["data"].values()))
            _run(env.env_response(
                messages + [Msg(role="assistant", content=json.dumps(
                    {"action":"answer","value":val,"evidence_ids":[body["evidence_id"]]}))], state))
            break
    assert state["episode"].done
    from rubric import grade
    assert grade(state["episode"])["total"] > 0.7

def test_bad_json_gets_error_observation():
    import x402_gym
    env = x402_gym.load_environment(tier="easy", num_examples=1)
    state = make_state(env)
    obs = _run(env.env_response(
        [Msg(role="assistant", content="I will just think out loud")], state))
    assert "error" in json.loads(obs[0]["content"])
