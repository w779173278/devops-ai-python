## DevOps AI Deep Agent (M1)

This repo contains the M1 foundations from the DevOps deep agent plan:

- Plan negotiation skill that always drafts and confirms a diagnostic plan.
- Log and metric sub-agents that can run in parallel.
- CLI orchestrator for quick local validation.
- DeepAgents-compatible factory (`build_devops_agent`) so you can run the graph with the official runtime.

### Quickstart (CLI demo)

```bash
uv venv
source .venv/bin/activate
uv pip install -e .

python main.py "checkout 服务 500 错误暴涨，帮我看看最近 15 分钟的情况" --auto-approve
```

Flags:
- `--service` / `--environment` / `--window`: scope defaults to checkout/production/15m.
- `--skip-logs` / `--skip-metrics`: disable a sub-agent.
- `--auto-approve`: skip plan confirmation prompt.

### DeepAgents runtime

```python
from devops_ai_python import build_devops_agent

agent = build_devops_agent()  # requires `deepagents` to be installed
result = agent.invoke({"messages": [{"role": "user", "content": "checkout 5xx in prod"}]})
```

Sub-agents:
- `log-analyst`: ELK sampling + clustering
- `metric-analyst`: Prometheus anomalies

The plan-negotiation skill is captured in `.deepagents/skills/plan-negotiation`.
