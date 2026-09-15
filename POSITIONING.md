# Positioning and sales routes (research-grounded, Sept 15 2026)

## Demand evidence

- Epoch AI (Jan 12 2026, interviews with 18 people across env startups,
  neolabs, frontier labs): Anthropic discussed $1B+/yr on RL environments
  (The Information, Sept 2025); tasks sell for $200-$2,000 each; exclusive
  deals run 4-5x non-exclusive; vendor contracts are six-to-seven
  figures/quarter. Growth areas: enterprise workflows, longer-horizon tasks,
  multi-turn interaction. Top quality bar: reward-hacking robustness,
  difficulty calibration (min ~2-3% pass, discard >70%), compositional skills.
  https://epoch.ai/gradient-updates/state-of-rl-envs
- Prime Intellect runs a paid Environments Program: open-access bounties
  $100-500 (lockable by anyone via PR), application-only bounties
  $1,000-$5,000+ requiring a demonstrated completed project.
  https://docs.google.com/spreadsheets/d/13UDfRDjgIZXsMI2s9-Lmn8KSMMsgk2_zsfju6cx_pNU
  Contributing guide: https://github.com/PrimeIntellect-ai/prime-environments/blob/main/docs/contributing.md
- Vendor directory for outreach/comps: https://www.rl-list.com/
  (Mechanize, Veris AI, etc.)
- Web3/agentic-payments security is documented as a live problem class:
  arxiv 2605.30998 "Free-Riding the Agentic Web" (systematic x402 security
  analysis), arxiv 2605.11781 "Five Attacks on x402", arxiv 2607.12575
  (population-scale x402 adoption measurement). Existing web3 RL work is
  trading-focused (FinRL etc.); nobody ships an agentic-payments safety
  environment. That is the gap this fills.

## Why this environment matches the buying criteria

- Reward-hack resistant: graders score the action log, not self-report;
  evidence-hash provenance; catastrophic key-export zeroing.
- Smooth difficulty gradient with verified feasibility ceiling and a
  scripted floor (see BENCHMARKS.md).
- Compositional: every tier reuses the same skills at higher pressure.
- Long-horizon multi-turn tool use with money at stake - the exact
  "enterprise workflow with real consequence" shape buyers describe.
- Extensible generator: thousands more instances by seed sweep; new scenario
  families are new tiers.

## Sales routes, in order of speed (corrected Sept 15 2026)

CORRECTION: the Prime Intellect bounty program is CLOSED. Verified today via
the program sheet's live CSV export: "This bounty program is closed and is not
accepting new applications or bounty claims" (both Open Access and
Application-Only). The earlier positioning assumed it was open.

1. Prime Intellect Environments Hub (live, not paid): publish x402-gym via the
   prime CLI / PR to PrimeIntellect-ai/prime-environments. Hub listing is the
   discoverability + credibility asset that unlocks vendor conversations;
   community envs are still merged there (38+ vendors track the ecosystem).
   https://app.primeintellect.ai/dashboard/environments
2. Direct licensing to RL environment vendors from the rl-list.com directory
   (38 companies: Mechanize, Veris AI, Mercor, Surge, etc.): non-exclusive
   license at documented task rates ($200-2,000/task), exclusive held-out
   variants at the 4-5x multiplier (seed-sweep generator makes per-buyer
   private sets practical). https://www.rl-list.com/
3. rl-list.com vendor listing for inbound once the repo is public.

## Companion credibility assets (already live)

- Field guide + scanner repo:
  https://github.com/OneDollarAgent/web3-auth-security-field-guide
- Live x402 scanner endpoint: https://web3-auth-scan.andrenorton.workers.dev
