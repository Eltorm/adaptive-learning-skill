# Adaptive Learning Skill

[English](README.md) | 简体中文

把任意主题、问题或切入点，转化为依赖关系清晰、深度自适应、关联有取舍、证据可追溯的学习路径与教学材料。

本仓库是建立在 V0.1 baseline 之上的 V0.2 可选状态协议。它主要是一套给 AI 使用的工作手册，并配有可移植的状态文件协议；它不是托管式数据库，也不是 Web 应用。整体设计遵循：

`信息 → 知识 → 课程 → 掌握`

## 功能

- 判断请求属于术语、概念、机制、方法、工具、子领域、领域还是跨学科问题，并按尺度控制范围；
- 从学习者当前已知内容或指定问题切入，不默认把整套基础课重新讲一遍；
- 在内部构建层级与依赖图，只把对当前目标有帮助的关联呈现给学习者；
- 适配数学、自然科学、计算机与工程、历史与社会科学、医学、法律、人文与艺术等领域，不强行套用单一学科模板；
- 使用 L0–L6 掌握深度，结合边界、反例、练习、重构、预测和迁移检查；
- 选择认知主线，并控制哪些关系作为主线、伏笔或延伸支线暴露；
- 对时效性、争议性、研究敏感、版本敏感或安全相关的内容进行证据分级与必要核查；
- 在学习者明确同意后，使用可移植 YAML 文件记录知识图、掌握证据、学习会话和复习队列。

## 使用方式

将此文件夹作为 Codex Skill 加载。可以直接使用自然语言，也可以使用以下可选模式：

```text
/learn 过拟合
/learn 法国大革命——我知道时间线，但不了解因果
/chapter 缩放点积注意力，目标 L3
/explain 为什么光合作用需要光反应和 Calvin 循环
/practice TCP 拥塞控制，目标 L4
/test PID 控制器
/review
```

Skill 内部保留比正文更丰富的知识图，但正文只沿着当前最优认知路径展开，因此不会把“相关概念”堆成列表。

## 仓库结构

- `SKILL.md`：运行时指令、工作流和各模式的输出契约；
- `references/`：输出协议、证据核查、领域适配、评估、认知路径、写作、状态管理和迭代路线；
- `schemas/`：概念、课程、证据、知识图和学习状态的可选 YAML 结构；
- `scripts/validate_state.py`：只读检查用户指定状态目录的完整性；
- `scripts/state_tool.py`：用于状态目录的显式 `init`、`record`、`due`、`merge-graph`、`export`、`import` 和 `validate` 操作；
- `examples/`：机器学习、强化学习、历史、生物和反例示范；
- `tests/`：跨领域案例、评分量表、契约检查、状态夹具和测试报告；
- `CHANGELOG.md`：按版本记录已实现内容与明确延期的功能；
- `README.md`：英文说明；
- `README.zh-CN.md`：本中文说明。

## 状态与隐私

Skill 默认无状态，只使用当前对话和学习者提供的进度。只有当学习者明确要求保存、继续、追踪或复习，并确认目录位置后，才应创建或修改状态文件。状态记录保存的是任务、评分维度、证据、时间和来源，而不是未经验证的“我会了”标记；冲突声明会被保留并标记为待复核。

示例状态流程（仅在学习者明确同意后执行）：

```powershell
python scripts/state_tool.py init .adaptive-learning
python scripts/state_tool.py validate .adaptive-learning
python scripts/state_tool.py due .adaptive-learning --at 2026-09-12
python scripts/state_tool.py export .adaptive-learning backup.zip
```

`export`、`import` 和图合并操作会拒绝覆盖已有目标，并保留冲突以便复核。托管搜索、外部提醒、多用户同步和自动化服务不在当前仓库的实现范围内。

## 迭代策略

V0.1 验证主题尺度、前置知识、知识图、深度控制、领域适配、可靠性和掌握评估这七项核心能力。V0.2 增加认知路径选择以及用户主动授权的文件状态。当前 V1.0 协议增加了可移植知识图合并和归档导入导出；托管式搜索、提醒和多人同步仍明确留在范围之外。

每次修改 Skill 后，都应使用至少三个不同领域的关键词运行跨领域测试，记录具体失败，并只提交由测试结果支持的最小规则改动。详见 [`references/iteration-roadmap.md`](references/iteration-roadmap.md) 和 [`tests/rubric.md`](tests/rubric.md)。

## 许可证

MIT，详见 [`LICENSE`](LICENSE)。
