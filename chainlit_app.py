"""Chainlit 前端：包装 DevOps 深度代理，实现多轮流式对话。"""

from __future__ import annotations

from typing import Any

import chainlit as cl

from devops_ai.agent import build_devops_agent


def _to_text(content: Any) -> str:
    """将消息内容转成文本，兼容 LangChain 的富内容结构。"""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for part in content:
            if isinstance(part, dict) and "text" in part:
                parts.append(str(part.get("text", "")))
            else:
                parts.append(str(part))
        return "\n".join(parts)
    return str(content)


@cl.on_chat_start
async def on_chat_start() -> None:
    agent = build_devops_agent()
    cl.user_session.set("agent", agent)
    cl.user_session.set("messages", [])
    await cl.Message(
        content="已启动 DevOps 主脑代理（可调度日志/Prometheus/代码子 Agent）。"
    ).send()


@cl.on_message
async def on_message(message: cl.Message) -> None:
    agent = cl.user_session.get("agent")
    if agent is None:
        agent = build_devops_agent()
        cl.user_session.set("agent", agent)

    messages: list[tuple[str, str]] = list(cl.user_session.get("messages") or [])
    messages.append(("user", message.content))

    reply = cl.Message(content="")
    last_ai_text: str | None = None

    try:
        async for event in agent.astream({"messages": messages}, stream_mode="values"):
            msg = event["messages"][-1]
            text = _to_text(getattr(msg, "content", msg))
            role = getattr(msg, "type", None) or getattr(msg, "role", None)
            if role in {"ai", "assistant"}:
                last_ai_text = text
                await reply.stream_token(text + "\n")
        await reply.send()
    except Exception as exc:  # noqa: BLE001
        await cl.Message(content=f"出错：{exc}").send()
        return

    if last_ai_text:
        messages.append(("assistant", last_ai_text))
        cl.user_session.set("messages", messages)
