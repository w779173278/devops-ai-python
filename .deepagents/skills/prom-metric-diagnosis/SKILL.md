---
name: prom-metric-diagnosis
description: 基于 Prometheus 的指标诊断与异常检测
---

# prom-metric-diagnosis

## 适用场景
- 已获 plan-negotiation 确认，需要对 Prometheus 指标做快速巡检/异常检测。

## 工具
- 使用 `prom_metric_snapshot(plan)` 工具按计划拉取指标，默认只读。

## 执行步骤
1. 根据 plan 的 service/environment/window_minutes 确定查询范围与对比基线。
2. 调用 `prom_metric_snapshot` 检查错误率、延迟、CPU、内存、QPS 等核心指标，识别尖刺/趋势/瓶颈。
3. 输出字段：`summary`、`key_findings`（文字化趋势）、`anomalies`（异常点 + 定性幅度）、`next_steps`、`confidence`（0-1）。
4. 提出可执行的下一步（加采样、扩容、回滚、继续观察），但不直接执行；需交由执行 Agent。

## 约束
- 不编造精确数值，仅给定性趋势或相对变化。
- 保持只读，不做变更；遇到缺口要明确说明。
