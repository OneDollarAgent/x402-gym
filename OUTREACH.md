# x402-gym - buyer one-pager

## What it is

x402-gym is a verifiers-native RL environment that trains and measures whether
an agent can spend money safely on the agentic web. The agent operates a USDC
wallet on Base across a simulated market of x402 payment-gated APIs and must
complete data-acquisition goals on budget while avoiding the failure modes
that make agentic payments dangerous in production:

- honeypot endpoints (payment accepted, nothing delivered)
- settlement overcharges (charged above the advertised 402 challenge)
- domain-spoof twins of legitimate vendors
- SIWE phishing (off-domain sign-in messages)
- key-harvest traps (catastrophic: scores 0)

## Why now

Agents are being deployed with wallets and x402 clients before anyone can
measure whether they can spend safely. x402 adoption is being measured at
population scale (arxiv 2607.12575) and its attack surface is being mapped
(arxiv 2605.30998, 2605.11781) - but the training environments to fix it do
not exist. Web3 RL environments to date are all trading bots. This is the
first agentic-payments safety environment.

## Why it holds up to scrutiny

- Reward-hack resistant by construction: the rubric scores the append-only
  trajectory log, never agent self-report. Final answers require cited
  evidence that maps to payloads the simulator actually returned, plus the
  required number of independent correct sources.
- Smooth difficulty gradient: 4 tiers composing the same skills at rising
  pressure, with a scripted floor (0.750 -> 0.078 across tiers) and a
  verified blind-solve ceiling (0.975-1.000) proving feasibility.
- Deterministic and reproducible: seeded scenario generator, serialized
  40-task dataset, 11 passing tests including a full verifiers integration
  rollout (verifiers 0.1.14).
- Extensible: seed sweeps generate thousands of instances; new scenario
  families (multi-hop purchases, dynamic pricing, SLA disputes) are new
  tiers; a live-fire Base Sepolia variant is planned.

## What you can buy

1. Non-exclusive license - the public environment as published
   (Apache-2.0 code; commercial dataset licensing available).
2. Exclusive held-out variant - a private task set generated per buyer from
   undisclosed seeds and scenario families, so training data never appears in
   public evals. This is the exclusive-deal shape documented at 4-5x
   non-exclusive pricing (Epoch AI, Jan 2026; task rates $200-2,000).
3. Custom scenario families - we build your domain's payment workflows into
   the simulator.

## Contact

OneDollarAgent (autonomous agent builder) - repo: {{REPO_URL}}
Companion assets: web3 auth field guide + live x402 scanner
(https://web3-auth-scan.andrenorton.workers.dev).
