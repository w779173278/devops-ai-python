"""DevOps deep agent with orchestrator + subagents."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from deepagents.middleware.subagents import SubAgent
from langchain.agents.middleware import InterruptOnConfig
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver

ORCHESTRATOR_PROMPT = """
你是 DevOps 主脑 Agent，负责规划→确认→调度子 Agent→汇总报告。
子 Agent 列表：
- log-collector：日志采集，抓取并总结指定服务/环境/时间窗口的异常日志。
- prometheus-collector：Prometheus 采集，查询指标并给出异常趋势。
- code-collector：代码采集，提取近期变更、模块与潜在风险。

当前上下文
当前时间: {}
工作流：
1) 收集服务基础信息（service、environment、时间窗口；可选 branch/commit）。
2) 先产出分析计划（每步写明子 Agent、输入参数、预期产出、缺口），等待用户确认。
3) 用户确认后，用 task 工具按步骤并行/串行调度子 Agent，缺信息先澄清。
4) 汇总报告：摘要；证据（指标/日志/代码，注明来源）；初步原因；下一步建议/确认口令。

规则：
- 未获确认前不要调用 task 子 Agent。
- 只基于子 Agent 返回的信息做结论，不要虚构；明确标注数据来源。
- 过程要简短进度提示，便于用户知晓执行阶段。
"""

LOG_AGENT_PROMPT = """
你是日志采集 Agent。目标：返回指定服务/环境/时间窗口的异常模式和样例。
输入至少包含：service、environment、window_minutes、limit（样例条数）。
输出包含：关键模式/计数、典型日志样例、可疑时间段。
缺少必要参数时直接报错说明缺口，不要臆测。
IMPORTANT: Return only the essential summary.
Do NOT include raw data, intermediate search results, or detailed tool outputs.
Your response should be under 500 words
"""

METRIC_AGENT_PROMPT = """
你是 Prometheus 采集 Agent。目标：返回指定服务/环境/时间窗口的核心指标趋势。
关注：error_rate、latency_p99_ms、cpu_percent、qps。
输出包含：峰值与基线、开始时间、异常描述、建议观察项。
缺少 service/environment/window_minutes 时直接说明缺口。
IMPORTANT: Return only the essential summary.
Do NOT include raw data, intermediate search results, or detailed tool outputs.
Your response should be under 500 words
"""

CODE_AGENT_PROMPT = """
你是代码采集 Agent。目标：返回近期代码变更摘要与潜在风险点。
输入至少包含 service；可选 branch、recent_commits。
输出包含：提交哈希、标题、涉及模块、风险提示。
若缺少 service，直接说明缺口。
IMPORTANT: Return only the essential summary.
Do NOT include raw data, intermediate search results, or detailed tool outputs.
Your response should be under 500 words
"""


@tool("collect_logs")
def collect_logs(
        service: str,
        environment: str,
        window_minutes: int = 30,
        limit: int = 30,
) -> dict[str, Any]:
    """日志采集工具（示例数据）。"""
    return {
        "agent": "log_collection",
        "service": service,
        "environment": environment,
        "window_minutes": window_minutes,
        "limit": limit,
        "insights": [
            "5xx/ERROR 占比较基线上升 220%，高峰出现在最近 10 分钟。",
            "主要模式：调用 api-gateway 超时；少量 NullPointer/序列化异常。",
        ],
        "samples": [
            "2024-01-01T12:04:11Z ERROR checkout timeout to api-gateway after 3.0s",
            "2024-01-01T12:05:02Z ERROR checkout NullPointer in payment adapter",
        ],
    }


@tool("collect_prom_metrics")
def collect_prom_metrics(
        service: str,
        environment: str,
        window_minutes: int = 30,
) -> dict[str, Any]:
    """Prometheus 采集工具（示例数据）。"""
    return {
        "service": service,
        "environment": environment,
        "window_minutes": window_minutes,
        "trends": {
            "error_rate": {"peak": "4.2%", "baseline": "0.3%", "since": "12:05Z"},
            "latency_p99_ms": {"peak": 850, "baseline": 220},
            "cpu_percent": {"peak": 92, "baseline": 55},
            "qps": {"peak": 1800, "baseline": 1200},
        }
    }


@tool("collect_code_changes")
def collect_code_changes(
        service: str,
        branch: str = "main",
        recent_commits: int = 3,
) -> dict[str, Any]:
    """代码采集工具（示例数据）。"""
    return {
        "agent": "code_collection",
        "service": service,
        "branch": branch,
        "recent_commits": recent_commits,
        "changes": [
            {
                "commit": "a1b2c3d",
                "title": "Add retry around api-gateway calls",
                "modules": ["checkout/api.py", "checkout/retry.py"],
                "risk": "高：可能导致放大重试与超时堆积",
            },
            {
                "commit": "d4e5f6g",
                "title": "Adjust payment adapter null handling",
                "modules": ["payment/adapter.py"],
                "risk": "中：可能引入 NullPointer 相关错误",
            },
        ],
        "notes": [
            "近 2 次提交涉及 api-gateway 调用与异常处理，建议与日志/指标交叉验证。",
        ],
    }


chat_model = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
)

SUBAGENTS: list[SubAgent] = [
    {
        "name": "log-collector",
        "description": "采集并总结指定服务/环境/时间窗口的异常日志模式与样例。",
        "system_prompt": LOG_AGENT_PROMPT,
        "tools": [collect_logs],
        "model": chat_model,
    },
    {
        "name": "prometheus-collector",
        "description": "查询 Prometheus 指标并输出异常趋势。",
        "system_prompt": METRIC_AGENT_PROMPT,
        "tools": [collect_prom_metrics],
        "model": chat_model,
    },
    {
        "name": "code-collector",
        "description": "提取近期代码变更、关联模块与潜在风险。",
        "system_prompt": CODE_AGENT_PROMPT,
        "tools": [collect_code_changes],
        "model": chat_model,
    },
]

# Checkpointer is REQUIRED for human-in-the-loop
checkpointer = MemorySaver()

def build_devops_agent(model: str | None = None):
    """创建一个包含主脑/子 Agent 调度的深度代理。"""
    return create_deep_agent(
        model=chat_model,
        system_prompt=ORCHESTRATOR_PROMPT.format(datetime.now()),
        subagents=SUBAGENTS,
        interrupt_on={
            "collect_logs": InterruptOnConfig(allowed_decisions=["approve", "reject"]),
        },
        debug=False,
        backend=FilesystemBackend(root_dir=".", virtual_mode=True),
        checkpointer=checkpointer,
    )
