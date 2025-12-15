---
name: plan-negotiation
description: 生成并协商诊断计划，得到用户明确确认后再调用子 Agent
---

# plan-negotiation

## 适用场景
- 任何诊断请求进入执行前，先生成并协商分析计划。
- 用户未提供服务/环境/时间窗等关键信息时，先补全假设。

## 工具
- 使用 deepagents 提供的 `draft_analysis_plan` 工具，输出需符合 `plan.schema.json`（service、environment、window_minutes、include_logs、include_metrics、outputs）。
- 默认只读，不触发真实操作。

## 操作步骤
1. 解析用户需求与假设：服务/环境/时间窗口/关注点（日志、指标），缺失则给出默认值供确认。
2. 调用 `draft_analysis_plan` 生成结构化 plan，并转写为编号要点（不超过 5 条），涵盖范围、日志分析、指标分析、输出形式。
3. 明确陈述成功定义（期望输出：summary、samples/趋势、原因、next steps）与风险/缺口。
4. 提供可直接复用的确认语句（参考 `confirm.phrases.md`），等待用户确认或修改。未确认禁止调用子任务。
5. 用户调整后更新 plan，再次确认，直到收到明确批准。

## 输出
- 结构化 plan（JSON 或表格形式）+ 编号简版计划。
- 明确的确认提示语，必须等待肯定回复再继续。

## 约束
- 未获确认不得调用日志/指标子 Agent。
- 保持简洁，不要冗长前置说明。
