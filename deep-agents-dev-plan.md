# LangChain Deep Agents 开发计划（精简版）

## 目标与范围

- 目标：用 LangChain 的 Deep Agents（基于 LangGraph 的可递归计划/执行/反思循环）实现 DevOps 对话助手，满足先给计划、用户确认后再调用日志/指标/执行工具的要求。
- 范围：聊天入口 → 计划生成/确认 → 工具调用（日志/指标/执行）→ 结果讲解 → 审计记录；不含具体监控/日志后端的生产接入，只做接口与演示级实现。

## 技术选型

- 语言/框架：Python 3.9+，LangChain 1.0+，LangGraph 0.1+，`langchain-openai` 作为默认 LLM 提供方。
- Deep Agents 结构：Planner（生成子任务与工具调用序列）→ Executor（调用工具）→ Reflector（反思/重试/继续搜索）→ Summarizer（面向用户输出）。
- 状态存储：LangGraph Checkpoint（SQLite 或文件），便于多轮对话记忆与可回溯性。
- 观测：基础日志（`structlog`）+ LangSmith/Langfuse 钩子预留。

## 里程碑与交付物

1. **基础搭建（0.5 天）**
   - 输出：`requirements.txt/pyproject` 更新，最小示例脚本可跑通 LLM 回声。
2. **Deep Agent 骨架（1 天）**
   - 输出：`app/agent_graph.py`，含状态定义、Planner/Executor/Reflector/Summarizer 节点，可跑通简单数学/搜索类工具。
3. **DevOps 工具封装（1 天）**
   - 输出：`app/tools/logs.py`、`metrics.py`、`actions.py`（先用 stub/假数据），工具接口与参数校验到位。
4. **对话与计划流程（0.5 天）**
   - 输出：`app/chat.py`，支持「生成计划→等待用户确认→按计划执行」的对话逻辑，含 SSE/流式输出占位。
5. **验证与文档（0.5 天）**
   - 输出：单元/集成测试样例（对 Planner、工具调用、确认分支），README/使用说明，示例对话脚本。

## 核心设计（Deep Agents 流程）

1. **状态定义**：`ConversationState` 包含 `messages`、`goals`、`plan`、`executions`、`observation`、`user_confirmed`、`retry_count`。
2. **Planner 节点**：根据用户输入与上下文生成有序子任务列表，标注所需工具和预期产出。首次进入必出计划并将 `user_confirmed=False`。
3. **确认钩子**：若 `user_confirmed` 为 False，则仅返回计划摘要，等待用户明确确认/修改；确认后写入状态并进入执行。
4. **Executor 节点**：逐条子任务调用对应 Tool（日志/指标/执行），产出 observation；失败则记录错误并交给 Reflector 决定是否重试或降级。
5. **Reflector 节点**：基于 LLM 简评当前 observation，决定 `continue` / `retry` / `stop`，可追加新子任务。
6. **Summarizer 节点**：面向用户汇报结果，结构包含：问题摘要、关键发现、工具证据链接/片段、建议动作、下一步确认口令。
7. **审计记录**：将 `plan`、`executions`、确认指令与工具输出写入 Checkpoint/文件，便于导出。

## 任务拆解与验收标准

- **依赖与配置（uv）**：`uv sync` 按 `pyproject.toml/uv.lock` 还原；新增依赖用 `uv add <pkg>`（会更新锁），更新指定包用 `uv lock --upgrade-package <pkg>`；OpenAI key 通过环境变量读取；验收：启动示例脚本可返回 LLM 响应。
- **图定义**：完成 LangGraph `StateGraph`，节点与边清晰，支持 Planner→(确认)→Executor↔Reflector→Summarizer；验收：运行示例时可按计划执行两步工具并生成总结。
- **工具层**：日志/指标/执行工具提供统一 `BaseTool` 封装，含参数校验与假数据返回；验收：传入缺失参数能给出友好报错，正常路径返回示例结构化结果。
- **对话体验**：CLI/HTTP 入口支持流式输出，首轮返回计划草案，用户输入“确认按计划执行”后继续；验收：手工对话可触发两轮工具调用并拿到汇总。
- **测试与文档**：提供最小单测（Planner 生成计划、确认分支、工具调用）、快速开始文档与示例对话；验收：`pytest` 通过，文档步骤可复现。

## 风险与缓解

- LLM 输出不稳：对计划/执行增加 schema 校验与重试上限，失败时回退到明确错误提示。
- 工具接口未就绪：以 stub 实现对外协议，先跑通代理链路；后续再接入真实数据源。
- 成本与时延：Planner/Reflector 默认使用小模型，可配置开关切换更强模型。

## 下一步

按里程碑依次推进，优先完成骨架与确认闭环，再替换真实工具与数据源，最后补充测试与文档。
