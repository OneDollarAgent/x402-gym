# Submission package: publishing + outreach

## A. Prime Intellect Environments Hub publish checklist

Verified against verifiers 0.1.14 and prime-environments conventions
(environments/<name>/<name>.py + pyproject.toml + README.md):

1. Repo is public under OneDollarAgent (GitHub).
2. `load_environment()` exposed at package root (x402_gym.py) - DONE.
3. JSON-action MultiTurnEnv with @vf.stop check_done, setup_state episode
   init, env_response observation loop - DONE, integration-tested locally.
4. Rubric: reward_total (weight 1.0) + zero-weight component metrics
   (completion/efficiency/safety/process) for trajectory inspection - DONE.
5. Publish flow (verified from Prime docs, Sept 15 2026):
   `prime login` (requires a Prime Intellect account - create an agent-owned
   one and set the profile username at app.primeintellect.ai/dashboard/profile),
   then from the repo root: `prime env push`. After upload, installable via
   `prime env install <owner>/x402-gym`. No URL/git dependencies to declare.
6. Local verification commands:
   - `python3 -m pytest tests/ -q` (11 passing: unit + vf integration)
   - `python3 scripts/run_baseline.py` (difficulty calibration)
   - hub-side: `uv run vf-eval x402_gym -n 1 -r 1` (needs an inference key;
     run by whoever publishes)
6. Draft PR to PrimeIntellect-ai/prime-environments with description:
   - "Novel environment: x402-gym trains agents to operate x402 payment-gated
     APIs safely (budgeted multi-turn tool use against honeypots, settlement
     overcharges, domain spoofs, SIWE phishing, key-harvest traps)."
   - vf.Environment = JSON-action MultiTurnEnv over a deterministic seeded
     simulator; vf.Rubric = trajectory-log grader with evidence-provenance
     checks (reward-hack resistant; key export zeroes the episode).
   - Calibration: scripted floor 0.08-0.75 by tier, verified feasibility
     ceiling 0.975-1.0 (BENCHMARKS.md).
   - Blockers: none known; live-fire Base Sepolia variant is future work.

## B. Vendor outreach (draft only - do not send without approval)

Direct-licensing targets, ranked, with exact routes (all verified live
Sept 15 2026):

1. Bespoke Labs - RL-environment curation for frontier labs, open-source
   friendly (OpenThoughts, Curator). Route: company@bespokelabs.ai
   (published on their own contact page, bespokelabs.ai/contact).
2. AfterQuery - supplies frontier labs with RL environments and publishes
   real-task benchmarks (Terminal-Bench, VADER). Route: contact form at
   https://www.afterquery.com/contact.
3. Veris AI - agent simulation infrastructure for enterprises; the
   payments-safety angle matches their reliability/compliance pitch.
   Route: demo request form at https://www.veris.ai/demo (Head of Sales:
   Kris Dickinson, per their company page).
4. Fleet AI - not a sale; a second distribution channel. DONE: a
   Harbor-format adapter now ships in-repo at harbor/ (task generator plus
   one oracle-validated task per tier, verified end-to-end through the
   container harness CLI: 0.975/1.0/1.0/1.0). Next step is a PR to
   github.com/fleet-ai/harbor adding the tasks.

Deprioritized: Mechanize (in-person SF hiring; builds in-house), Huzzle
(primarily a talent marketplace), Mercor/Surge/Handshake/Turing (staffing-
scale model; weak fit for a single-environment license).

Pitch skeleton (one short paragraph + link):
"OneDollarAgent built x402-gym, a verifiers-native RL environment for
agentic-payments safety: 40 seeded tasks across 4 difficulty tiers,
trajectory-log grading with evidence provenance, scripted calibration
(floor 0.08, ceiling 1.0). Available non-exclusive, or exclusive with a
held-out private task set generated per buyer. Repo: https://github.com/OneDollarAgent/x402-gym."

Pricing anchor (Epoch AI, Jan 2026): $200-2,000 per task; exclusivity 4-5x.

## C. rl-list.com inbound listing

Once public, submit the repo/vendor profile for directory inclusion.
