# Project Knowledge Base

> [中文](#中文) · [English](#english)

---

<a id="中文"></a>

## 中文

### 这是什么

**Project Knowledge Base** 是一套让 AI 编码助手跨任务、跨上下文压缩「不丢记忆」的标准作业流程（SOP / Skill）。它把项目记忆当作**可维护的工程状态**，而不是聊天记录：初始化、恢复、审计、长期维护一个结构化的知识库，覆盖项目事实、决策、悬而未决的硬件相关工作、调试陷阱与证据。

当你的项目很长、上下文会被压缩、或者需要换一个新会话/新 AI 接管时，它尤其有用。

### 核心特性

- **初始化一次**：把知识库脚手架（模板文件）安装进你的项目，并自动在 `AGENTS.md` 注入维护指令，让后续 AI 自动接管记忆维护。
- **每次任务维护**：在任务开始读取知识库，在关键事实/决策/根因/部署/回滚后即时更新，绝不把未完成的事项静默丢弃。
- **专用记忆车道**：当前事实、决策、诊断证据、开放问题、调试陷阱、延迟工作台账各自独立，互不混淆。
- **可恢复**：上下文压缩或会话中断后，从知识库和真实项目证据重建状态，而不是凭聊天记忆猜测。
- **边界约束**：不存密码/令牌/密钥，不把大日志塞进出入口文档，不把推断当作已验证事实，不擅自「解决」延迟工作。

### 目录结构

```
project-knowledge-base/
├── SKILL.md                              # 维护 SOP（核心规则）
├── agents/openai.yaml                    # Agent 接口定义
├── references/                          # 详细规范
│   ├── initialization.md                # 初始化流程
│   ├── maintenance-protocol.md          # 维护协议（字段与压缩规则）
│   └── memory-model.md                  # 记忆模型与真理层级
├── scripts/
│   ├── bootstrap_project_knowledge.py   # 安装 Skill + 引导知识库
│   └── audit_project_knowledge.py       # 结构/初始化状态审计
└── assets/                              # 模板与片段
    ├── PROJECT_MEMORY.md
    ├── AGENTS.snippet.md
    └── knowledge-base/                  # 各记忆车道模板
```

安装到目标项目后，结构变为：

```
<your-project>/
├── AGENTS.md                            # 自动注入维护指令
├── PROJECT_MEMORY.md                    # 知识库总入口
├── knowledge-base/                      # 各记忆车道
└── .agents/skills/project-knowledge-base/   # Skill 运行时
```

### 快速开始

把本仓库下载到你的项目**父目录**中（不要放进它自己的子目录），然后：

```bash
# 1. 安装 Skill 并引导知识库（仅创建缺失文件，非破坏式）
python scripts/bootstrap_project_knowledge.py --project-root /path/to/your-project

# 2. 审计结构并修复所有错误
python scripts/audit_project_knowledge.py --project-root /path/to/your-project
```

随后阅读 `SKILL.md`、`references/initialization.md`，把模板占位符替换为经核实、带来源链接的真实内容。

### 前置要求

- Python 3（仅运行脚本需要；也可用人工方式完成等效操作）。
- 任意支持 `AGENTS.md` / `.agents/skills/` 的 AI 编码助手（如 CodeBuddy、OpenAI 等）。

### 许可证

[MIT](LICENSE) © 2026 ShiYaoL

---

<a id="english"></a>

## English

### What is this

**Project Knowledge Base** is a standard operating procedure (SOP / Skill) that lets AI coding assistants keep durable project memory across tasks and context compaction. It treats project memory as **maintained engineering state**, not a chat transcript: initialize, recover, audit, and continuously maintain a structured knowledge base covering project facts, decisions, unresolved hardware-dependent work, debugging pitfalls, and evidence.

It is especially useful for long projects, projects whose context gets compacted, or when you need a fresh session / new AI to take over.

### Key features

- **Initialize once**: installs the knowledge-base scaffold into your project and auto-injects maintenance instructions into `AGENTS.md`, so future AI sessions maintain memory automatically.
- **Maintain every task**: reads the knowledge base at task start and updates it after material facts, decisions, root causes, deployments, or rollbacks — never silently drops unfinished work.
- **Dedicated memory lanes**: current facts, decisions, diagnostic evidence, open questions, debugging pitfalls, and a deferred-work ledger stay separate.
- **Recoverable**: after context compaction or session interruption, reconstruct state from the knowledge base and live project evidence instead of guessing from chat memory.
- **Boundaries**: never store passwords/tokens/keys, never dump large logs into entry docs, never treat an inference as a verified fact, never resolve deferred work on its own.

### Repository structure

```
project-knowledge-base/
├── SKILL.md                              # Maintenance SOP (core rules)
├── agents/openai.yaml                    # Agent interface definition
├── references/                          # Detailed specs
│   ├── initialization.md                # Initialization flow
│   ├── maintenance-protocol.md          # Maintenance protocol (fields & compaction)
│   └── memory-model.md                  # Memory model & truth hierarchy
├── scripts/
│   ├── bootstrap_project_knowledge.py   # Install Skill + bootstrap knowledge base
│   └── audit_project_knowledge.py       # Structure / init-state audit
└── assets/                              # Templates and snippets
    ├── PROJECT_MEMORY.md
    ├── AGENTS.snippet.md
    └── knowledge-base/                  # Memory-lane templates
```

After installation into a target project, the layout becomes:

```
<your-project>/
├── AGENTS.md                            # Auto-injected maintenance block
├── PROJECT_MEMORY.md                    # Knowledge base entry point
├── knowledge-base/                      # Memory lanes
└── .agents/skills/project-knowledge-base/   # Skill runtime
```

### Quick start

Download this repo into the **parent** directory of your project (not inside one of its own subdirectories), then:

```bash
# 1. Install the Skill and bootstrap the knowledge base (non-destructive; only creates missing files)
python scripts/bootstrap_project_knowledge.py --project-root /path/to/your-project

# 2. Audit the structure and repair every error
python scripts/audit_project_knowledge.py --project-root /path/to/your-project
```

Then read `SKILL.md` and `references/initialization.md`, and replace the scaffold placeholders with verified, source-linked content.

### Requirements

- Python 3 (only needed to run the scripts; equivalent operations can be done by hand).
- Any AI coding assistant that supports `AGENTS.md` / `.agents/skills/` (e.g. CodeBuddy, OpenAI, etc.).

### License

[MIT](LICENSE) © 2026 ShiYaoL
