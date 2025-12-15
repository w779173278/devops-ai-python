---
name: elk-log-analysis
description: ELK 日志诊断，采样 + 模式聚类，输出可执行的排查建议
---

# elk-log-analysis

## 适用场景
- 已通过 plan-negotiation 确认计划，需要在时间窗口内排查 5xx/错误日志。
- 需要代表性样例而非全量日志。

## 工具
- 使用 `elk_log_sampling(plan)` 工具按计划采样/聚类日志；保持脱敏和只读。

## 执行步骤
1. 读取确认后的 plan（service、environment、window_minutes），聚焦 5xx/ERROR 等高优先级事件。
2. 调用 `elk_log_sampling` 进行采样与模式聚类，样本控制在 3-5 条，附出现频次/影响面（大致级别即可）。
3. 输出字段：`summary`、`sample_logs`（模式描述 + redacted 示例）、`probable_causes`、`next_steps`、`confidence`（0-1）。
4. 标注需实操的动作并移交执行 Agent；本 skill 不直接执行。

## 约束
- 禁止输出全量或含敏感字段的日志，只给脱敏片段。
- 保持摘要化，避免上下文冗长。
- 不编造日志，按照实际日志返回分析。