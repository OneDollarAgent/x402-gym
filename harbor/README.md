# Harbor adapter

x402-gym tasks in the Harbor task format (github.com/fleet-ai/harbor, from the
Terminal-Bench creators): each task is a containerized directory with
`task.toml`, `instruction.md`, `environment/` (Dockerfile + harness +
scenario), `solution/` (oracle), and `tests/` (verifier writing
/logs/verifier/reward.txt).

Inside the container the agent drives the simulator through
`python3 /app/harness.py <action> '<json-args>'`; state persists in
/app/state (trajectory.jsonl + episode.pkl). The verifier grades the
trajectory with the same rubric as the verifiers environment and passes at
the tier threshold.

- `generate_tasks.py` mints task directories from `tasks/dataset.json`
  (default: one per difficulty tier; pass tier names for more).
- Oracle validation on host: the four generated tasks score
  0.975 / 1.000 / 1.000 / 1.000 through the CLI, proving feasibility.
- Harbor runner usage: `harbor run --path harbor/tasks/x402-gym-medium-01
  --agent <agent> --model <model>`.
