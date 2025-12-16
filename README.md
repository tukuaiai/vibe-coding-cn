<!--
-------------------------------------------------------------------------------
  项目头部区域 (HEADER)
-------------------------------------------------------------------------------
-->
<p align="center">
  <!-- 建议尺寸: 1280x640px。可以使用 Canva, Figma 或 https://banners.beyondco.de/ 等工具制作 -->
  <img src="https://github.com/tukuaiai.png" alt="Vibe Coding 指南" width="80px">
</p>

<div align="center">

# Vibe Coding 指南

**一个旨在通过与 AI 结对编程，将概念转化为现实的综合工作流程**

---

<!--
  徽章区域 (BADGES)
-->
<p>
  <a href="https://github.com/tukuaiai/vibe-coding-cn/actions"><img src="https://img.shields.io/github/actions/workflow/status/tukuaiai/vibe-coding-cn/main.yml?style=for-the-badge" alt="构建状态"></a>
  <a href="https://github.com/tukuaiai/vibe-coding-cn/releases"><img src="https://img.shields.io/github/v/release/tukuaiai/vibe-coding-cn?style=for-the-badge" alt="最新版本"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/tukuaiai/vibe-coding-cn?style=for-the-badge" alt="许可证"></a>
  <a href="https://github.com/tukuaiai/vibe-coding-cn"><img src="https://img.shields.io/github/languages/top/tukuaiai/vibe-coding-cn?style=for-the-badge" alt="主要语言"></a>
  <a href="https://github.com/tukuaiai/vibe-coding-cn"><img src="https://img.shields.io/github/languages/code-size/tukuaiai/vibe-coding-cn?style=for-the-badge" alt="代码大小"></a>
  <a href="https://github.com/tukuaiai/vibe-coding-cn/graphs/contributors"><img src="https://img.shields.io/github/contributors/tukuaiai/vibe-coding-cn?style=for-the-badge" alt="贡献者"></a>
  <a href="https://t.me/glue_coding"><img src="https://img.shields.io/badge/chat-telegram-blue?style=for-the-badge&logo=telegram" alt="交流群"></a>
</p>

[📚 相关文档](#-相关文档与资源)
[🚀 入门指南](#-入门指南)
[⚙️ 完整设置流程](#️-完整设置流程)
[📞 联系方式](#-联系方式)
[✨ 支持项目](#-支持项目)
[🤝 参与贡献](#-参与贡献)

本仓库的 AI 解读链接：[zread.ai/tukuaiai/vibe-coding-cn](https://zread.ai/tukuaiai/vibe-coding-cn/1-overview)

</div>

---

## 🖼️ 概览

**Vibe Coding** 是一个与 AI 结对编程的综合工作流程，旨在帮助开发者高效地将想法付诸实践。本指南详细介绍了从项目构思、技术选型、实施规划到具体开发、调试和扩展的全过程，强调以**规划驱动**和**模块化**为核心，避免因缺乏有效管理而导致项目陷入混乱。

> **核心理念**: *规划是项目成功的基石。* 审慎地引导 AI 进行规划，以确保代码库的可维护性和可管理性。

**注意**：以下经验分享并非普遍适用，请在具体实践中结合场景，辩证采纳。

## 🔑 元方法论 (Meta-Methodology)

该思想的核心是构建一个能够**自我优化**的 AI 系统。其递归本质可分解为以下步骤：

#### 1. 定义核心角色：

*   **α-提示词 (生成器)**: 一个“母体”提示词，其唯一职责是**生成**其他提示词或技能。
*   **Ω-提示词 (优化器)**: 另一个“母体”提示词，其唯一职责是**优化**其他提示词或技能。

#### 2. 描述递归的生命周期：

1.  **创生 (Bootstrap)**:
    *   使用 AI 生成 `α-提示词` 和 `Ω-提示词` 的初始版本 (v1)。

2.  **自省与进化 (Self-Correction & Evolution)**:
    *   使用 `Ω-提示词 (v1)` **优化** `α-提示词 (v1)`，从而得到一个更强大的 `α-提示词 (v2)`。

3.  **创造 (Generation)**:
    *   使用**进化后的** `α-提示词 (v2)` 生成所有需要的目标提示词和技能。

4.  **循环与飞跃 (Recursive Loop)**:
    *   将新生成的、更强大的产物（甚至包括新版本的 `Ω-提示词`）反馈给系统，再次用于优化 `α-提示词`，从而启动下一轮进化。

#### 3. 终极目标：

通过此持续的**递归优化循环**，系统在每次迭代中实现**自我超越**，无限逼近预设的**理想状态**。

## 🧭 原则 (Principles)

*   **自动化优先**: 优先利用 AI 自动化可执行的任务。
*   **AI 咨询**: 将 AI 作为首要信息来源和问题解决方案的顾问。
*   **目标驱动**: 开发过程中的所有活动都应围绕既定目标展开。
*   **上下文决定质量**: 上下文的质量直接决定输出的质量（GIGO原则）。
*   **系统性思维**: 从“实体”、“链接”、“功能/目的”三个维度进行系统性思考。
*   **编程的本质**: 数据结构与算法是编程的核心。
*   **流程化**: 使用“输入 -> 处理 -> 输出”的模式来刻画整个工作流程。
*   **深度提问**: 频繁向 AI 提出“是什么？”、“为什么？”、“怎么做？”以深化理解。
*   **规划先行**: 先构建清晰的结构和框架，再进行编码，以避免后期产生技术债务。
*   **奥卡姆剃刀**: 如无必要，勿增实体。保持代码简洁。
*   **帕累托法则 (80/20 Rule)**: 关注项目中那 20% 的关键部分。
*   **逆向工程**: 从最终需求出发，逆向构建解决方案。
*   **迭代与容错**: 鼓励多次尝试，在遇到困难时考虑重置环境或另辟蹊径。
*   **专注单一任务**: 保持高度专注，一次只解决一个问题，以确保深度和质量。

## 🧩 方法 (Methods)

*   **明确边界**: 清晰定义任务的目标和非目标。
*   **正交性**: 确保功能模块之间职责明确，减少重叠（视具体场景而定）。
*   **重用优于重写**: 遵循 DRY 原则，优先寻找并复用现有解决方案，而非重复构建。
*   **官方文档优先**: 在开发前，优先获取并利用官方文档作为 AI 的上下文。
*   **按职责划分模块**: 基于单一职责原则进行模块拆分。
*   **接口与实现分离**: 先定义接口，再实现具体逻辑。
*   **增量式修改**: 每次只修改一个模块，便于追踪和调试。
*   **文档即上下文**: 将文档撰写融入开发流程，而不是事后补充。

## 🛠️ 技术 (Techniques)

*   **明确变更范围**: 在指令中清晰说明允许修改和禁止修改的边界。
*   **标准化调试信息**: 进行调试时，请提供“预期结果”、“实际表现”及“最小可复现示例”。
*   **AI 辅助测试**: 可委托 AI 生成测试用例，但断言部分需要人工审查。
*   **隔离会话**: 当代码库变得复杂时，为不同任务切换独立的会话以保持上下文纯净。

## 📋 工具集 (Toolset)

*   [**Visual Studio Code**](https://code.visualstudio.com/): 功能强大的集成开发环境，适合代码阅读与手动修改。其 `Local History` 插件对新手尤其友好。
*   **虚拟环境 (.venv)**: 强烈推荐使用，通过指令要求 AI 在虚拟环境中安装和运行依赖，可实现项目环境的一键配置与隔离，特别适用于 Python 开发。
*   [**Claude 3 Opus**](https://claude.ai/): 在 Claude Code 等平台中使用，性能强大，响应迅速，提供 CLI 和 IDE 插件。
*   [**GPT-4/GPT-5 Series**](https://chat.openai.com/): 在专用平台（如 Codex CLI）中使用，适用于处理大型项目和复杂逻辑。
*   [**Gemini Advanced/Pro**](https://gemini.google.com/): 可通过 Gemini CLI 或 Google AI Studio 等多种渠道访问，适合执行脚本、整理文档和探索思路。
*   [**Ollama**](https://ollama.com/): 本地大模型管理工具，可通过命令行方便地拉取和运行开源模型。
*   [**Warp**](https://www.warp.dev/): 集成 AI 功能的现代化终端，能有效提升命令行操作和错误排查的效率。
*   [**Augment**](https://app.augmentcode.com/): 提供强大的上下文引擎和提示词优化功能，有助于新手和懒人快速生成高质量指令。
*   [**Cursor**](https://cursor.com/): 深度集成 AI 功能的 IDE，已获得广泛的用户认可。
*   **提示词库**:
    *   [**在线表格**](https://docs.google.com/spreadsheets/d/1ngoQOhJqdguwNAilCl1joNwTje7FWWN9WiI2bo5VhpU/edit?gid=2093180351#gid=2093180351&range=A1): 提供大量可直接复制使用的提示词。
    *   [**第三方系统提示词库**](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools): 用于学习其他AI工具的系统提示词。
*   **技能与模板**:
    *   [**Skills 生成器**](https://github.com/yusufkaraaslan/Skill_Seekers): 可根据需求生成定制化的 Skills。
    *   [**元提示词**](https://docs.google.com/spreadsheets/d/1ngoQOhJqdguwNAilCl1joNwTje7FWWN9WiI2bo5VhpU/edit?gid=1770874220#gid=1770874220): 用于生成提示词的提示词。
    *   [**通用项目架构模板**](./documents/通用项目架构模板.md): 可用于快速搭建标准化的项目目录结构。
*   **辅助工具**:
    *   [**Mermaid Chart**](https://www.mermaidchart.com/): 用于将文本转换为架构图、序列图等可视化图表。
    *   [**NotebookLM**](https://notebooklm.google.com/): 用于 AI 解读资料、音频和生成思维导图。
    *   [**Zread**](https://zread.ai/): AI 驱动的 GitHub 仓库阅读工具，有助于快速理解项目和减少重复开发。
    *   [**tmux**](https://github.com/tmux/tmux): 强大的终端复用工具，支持会话保持、分屏和后台任务，是服务器与多项目开发的利器。
    *   [**Neovim (nvim)**](https://github.com/neovim/neovim): 高性能的现代化 Vim 编辑器，拥有丰富的插件生态，是键盘流开发者的首选。
    *   [**LazyVim**](https://www.lazyvim.org/): 开箱即用的 Neovim 配置框架，预置了 LSP、代码补全、调试等全套功能。
    *   [**DBeaver**](https://dbeaver.io/): 通用数据库管理客户端，支持多种数据库，功能全面，是后端与数据工程师的必备工具。

---

## 编码模型性能分级参考

建议只选择第一梯队模型处理复杂任务，以确保最佳效果与效率。

*   **第一梯队**: `codex-5.1-max-xhigh`, `claude-opus-4.5-xhigh`, `gpt-5.2-xhigh`
*   **第二梯队**: `claude-sonnet-4.5`, `kimi-k2-thinking`, `minimax-m2`, `glm-4.6`, `gemini-3.0-pro`, `gemini-2.5-pro`
*   **第三梯队**: `qwen3`, `SWE`, `grok4`

---

## 📚 相关文档与资源

*   **交流社区**:
    *   [Telegram 交流群](https://t.me/glue_coding)
    *   [Telegram 频道](https://t.me/tradecat_ai_channel)
*   **个人分享**:
    *   [我的学习经验](./documents/学习经验.md)
    *   [编程书籍推荐](./documents/编程书籍推荐.md)
*   **核心资源**:
    *   [**元提示词库**](https://docs.google.com/spreadsheets/d/1ngoQOhJqdguwNAilCl1joNwTje7FWWN9WiI2bo5VhpU/edit?gid=1770874220#gid=1770874220): 用于生成提示词的高级提示词集合。
    *   [**元技能 (Meta-Skill)**](./skills/claude-skills/SKILL.md): 用于生成 Skills 的 Skill。
    *   [**技能库 (Skills)**](./skills): 可直接集成的模块化技能仓库。
    *   [**技能生成器**](https://github.com/yusufkaraaslan/Skill_Seekers): 将任何资料转化为 Agent 可用技能的工具。
    *   [**在线提示词数据库**](https://docs.google.com/spreadsheets/d/1ngoQOhJqdguwNAilCl1joNwTje7FWWN9WiI2bo5VhpU/edit?gid=2093180351#gid=2093180351&range=A1): 包含数百个适用于各场景的用户及系统提示词的在线表格。
    *   [**第三方系统提示词仓库**](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools): 汇集了多种 AI 工具的系统提示词。
*   **项目内部文档**:
    *   [**prompts-library 工具说明**](./libs/external/prompts-library/): 该工具支持在 Excel 和 Markdown 格式之间转换提示词，并包含数百个精选提示词。
    *   [**coding_prompts 集合**](./prompts/coding_prompts/): 适用于 Vibe Coding 流程的专用提示词。
    *   [**系统提示词构建原则**](./documents/系统提示词构建原则.md): 关于如何构建高效、可靠的 AI 系统提示词的综合指南。
    *   [**开发经验总结**](./documents/开发经验.md): 包含变量命名、文件结构、编码规范、架构原则等实践经验。
    *   [**通用项目架构模板**](./documents/通用项目架构模板.md): 提供多种项目类型的标准目录结构与最佳实践。
    *   [**Augment MCP 配置文档**](./documents/auggie-mcp配置文档.md): Augment 上下文引擎的详细配置说明。
    *   [**system_prompts 集合**](./prompts/system_prompts/): 用于指导 AI 开发的系统提示词，包含多个版本的开发规范与思维框架。

---

### 项目目录结构概览

`vibe-coding-cn` 项目的核心是围绕知识管理、AI 提示词的组织与自动化而构建。以下是其简化的目录结构说明：

```
.
├── backups/                     # 项目备份脚本。
├── documents/                   # 各类说明文档、经验总结和配置详情。
├── libs/                        # 通用库代码，包含内部模块和外部工具。
│   ├── common/                  # 通用功能模块。
│   ├── database/                # 数据库相关模块。
│   └── external/                # 外部集成工具，如 prompts-library。
├── prompts/                     # 核心资产：集中管理的各类型 AI 提示词。
│   ├── coding_prompts/          # 编程与代码生成专用提示词。
│   ├── system_prompts/          # AI 系统级行为与框架提示词。
│   └── user_prompts/            # 用户自定义提示词。
├── skills/                      # 模块化技能库，提供特定领域的工具和知识。
│
├── .gitignore                   # Git 忽略文件配置。
├── AGENTS.md                    # AI Agent 的行为准则与配置。
├── CLAUDE.md                    # Claude 模型的核心行为准则与配置。
├── CODE_OF_CONDUCT.md           # 社区行为准则。
├── CONTRIBUTING.md              # 贡献指南。
├── GEMINI.md                    # Gemini 模型的上下文与指令。
├── LICENSE                      # 项目开源许可证。
├── Makefile                     # 项目自动化任务脚本（如代码检查、备份）。
└── README.md                    # 项目主文档。
```

---

## ⚙️ 架构与工作流程

Vibe Coding 的核心工作流可以概括为：**规划驱动 + 上下文固定 + AI 结对执行**。它旨在将“从想法到可维护代码”的过程转变为一个可审计、可迭代的流水线。

**您将获得**:
- **成体系的提示词工具链**: 利用 `system_prompts` 约束 AI 行为边界，`coding_prompts` 提供从需求澄清、规划到执行的全链路支持。
- **闭环交付路径**: 遵循“需求 -> 上下文文档 -> 实施计划 -> 分步实现 -> 测试 -> 进度记录”的流程，确保全程可追溯、可移交。

```mermaid
graph TB
  subgraph ext_layer[外部系统与数据源层]
    ext_contrib[社区贡献者]
    ext_sheet[Google 表格 / 外部表格]
    ext_md[外部 Markdown 提示词]
    ext_api[预留：其他数据源 / API]
    ext_contrib --> ext_sheet
    ext_contrib --> ext_md
    ext_api --> ext_sheet
  end

  subgraph ingest_layer[数据接入与采集层]
    excel_raw[prompt_excel/*.xlsx]
    md_raw[prompt_docs/外部MD输入]
    excel_to_docs[prompts-library/scripts/excel_to_docs.py]
    docs_to_excel[prompts-library/scripts/docs_to_excel.py]
    ingest_bus[标准化数据帧]
    ext_sheet --> excel_raw
    ext_md --> md_raw
    excel_raw --> excel_to_docs
    md_raw --> docs_to_excel
    excel_to_docs --> ingest_bus
    docs_to_excel --> ingest_bus
  end

  subgraph core_layer[数据处理与智能决策层 / 核心]
    ingest_bus --> validate[字段校验与规范化]
    validate --> transform[格式映射转换]
    transform --> artifacts_md[prompt_docs/规范MD]
    transform --> artifacts_xlsx[prompt_excel/导出XLSX]
    orchestrator[main.py · scripts/start_convert.py] --> validate
    orchestrator --> transform
  end

  subgraph consume_layer[执行与消费层]
    artifacts_md --> catalog_coding[prompts/coding_prompts]
    artifacts_md --> catalog_system[prompts/system_prompts]
    artifacts_md --> catalog_assist[prompts/assistant_prompts]
    artifacts_md --> catalog_user[prompts/user_prompts]
    artifacts_md --> docs_repo[documents/*]
    artifacts_md --> new_consumer[预留：其他下游渠道]
    catalog_coding --> ai_flow[AI 结对编程流程]
    ai_flow --> deliverables[项目上下文 / 计划 / 代码产出]
  end

  subgraph ux_layer[用户交互与接口层]
    cli[CLI: python main.py] --> orchestrator
    makefile[Makefile 任务封装] --> cli
    readme[README.md 使用指南] --> cli
  end

  subgraph infra_layer[基础设施与横切能力层]
    git[Git 版本控制] --> orchestrator
    backups[backups/一键备份.sh · backups/快速备份.py] --> artifacts_md
    deps[requirements.txt · scripts/requirements.txt] --> orchestrator
    config[prompts-library/scripts/config.yaml] --> orchestrator
    monitor[预留：日志与监控] --> orchestrator
  end
```

---

<details>
<summary>📈 性能基准 (可选)</summary>

本仓库主要关注流程与提示词质量，而非代码性能。建议通过以下可观测指标进行追踪（当前依赖人工记录）：

| 指标 | 含义 | 建议记录方式 |
|:---|:---|:---|
| 提示命中率 | 一次生成即满足验收标准的比例。 | 在任务完成后于 `progress.md` 中记录 0/1。 |
| 周转时间 | 从需求提出到首个可运行版本所需的时间。 | 通过录屏或 CLI 定时器进行统计。 |
| 变更可追溯性 | 是否同步更新了上下文、进度及备份。 | 通过手动更新或在备份脚本中集成版本标签实现。 |
| 示例覆盖率 | 是否为每个模块提供了最小可运行示例或测试用例。 | 建议每个示例项目都包含独立的 README 和测试。 |

</details>

---

## 🗺️ 路线图

```mermaid
gantt
    title 项目发展路线图
    dateFormat YYYY-MM
    section 近期 (2025)
    补全演示GIF与示例项目: active, 2025-12, 15d
    prompts 索引自动生成脚本: 2025-12, 10d
    section 中期 (2026 Q1)
    一键演示/验证 CLI 工作流: 2026-01, 15d
    备份脚本增加快照与校验: 2026-01, 10d
    section 远期 (2026 Q1-Q2)
    模板化示例项目集: 2026-02, 20d
    多模型对比与评估基线: 2026-02, 20d
```

---

## 🚀 入门指南
*本节内容源自原作者，并根据当前推荐模型进行了更新。*

要开始使用 Vibe Coding，您需要以下任一工具：
- **Claude 3 Opus** (在 Claude Code 等平台使用)
- **GPT-4/GPT-5 系列模型** (在 Codex CLI 等平台使用)

本指南适用于 CLI 终端版本和 VSCode 扩展版本。

---

<details>
<summary><strong>⚙️ 完整设置流程</strong></summary>

<details>
<summary><strong>1. 创建项目设计文档</strong></summary>

-   将您的项目创意提交给 AI，并要求其生成一份简洁的 Markdown 格式**设计文档**（例如 `product-requirement-document.md`）。
-   审查并完善该文档，确保其与您的愿景一致。初期版本可以简略，其核心目标是为 AI 提供关于项目结构和意图的上下文。

</details>

<details>
<summary><strong>2. 确定技术栈并配置 AI 行为准则</strong></summary>

-   让 AI 为您的项目推荐**最简单且最健壮**的技术栈，并保存为 `tech-stack.md`。
-   在 AI 交互工具（如 Claude Code 或 Codex CLI）中，使用 `/init` 命令初始化 AI 的行为准则，使其读取您已创建的 `.md` 文件。
-   **关键步骤**: 审查并调整生成的规则，确保其强调**模块化**并禁止生成**单体巨文件**。部分核心规则必须设为始终应用（"Always"），以强制 AI 在编码前阅读关键上下文文档。

</details>

<details>
<summary><strong>3. 制定实施计划</strong></summary>

-   将设计文档和技术栈文档提供给 AI。
-   要求 AI 生成一份详细的 Markdown 格式**实施计划**，其中包含一系列给开发者的分步指令。
    -   每一步都应小而具体，并包含验证其正确性的测试方法。
    -   计划中只应包含清晰的指令，而非代码。
    -   初期聚焦于**核心功能**的实现。

</details>

<details>
<summary><strong>4. 构建记忆库 (Memory Bank)</strong></summary>

-   在项目根目录下创建 `memory-bank` 子文件夹。
-   将以下文件存入该文件夹：
    -   `product-requirement-document.md`
    -   `tech-stack.md`
    -   `implementation-plan.md`
    -   `progress.md` (空文件，用于记录开发进度)
    -   `architecture.md` (空文件，用于记录系统架构)

</details>

</details>

<details>
<summary><strong>💻 Vibe Coding 开发流程</strong></summary>

现在，我们开始核心开发流程。

<details>
<summary><strong>1. 澄清与确认</strong></summary>

-   启动 AI 交互工具。
-   **提问**: "请阅读 `/memory-bank` 文件夹中的所有文档。`implementation-plan.md` 的内容是否完全清晰？您有哪些问题需要我澄清，以确保计划对您而言是 100% 明确的？"
-   在回答完 AI 的所有问题后，让其根据您的回答更新 `implementation-plan.md`。

</details>

<details>
<summary><strong>2. 执行第一步</strong></summary>

-   **提问**: "请阅读 `/memory-bank` 中的所有文档，并执行实施计划的第 1 步。测试将由我负责。在测试通过之前，请不要开始第 2 步。验证通过后，请在 `progress.md` 中记录已完成的工作，并在 `architecture.md` 中更新架构信息。"
-   建议使用 "Ask" 或 "Plan" 模式，在 AI 执行前确认其计划。

</details>

<details>
<summary><strong>3. 迭代工作流</strong></summary>

-   完成第 1 步后，提交代码变更到 Git。
-   开始新的会话，并提问："请阅读 memory-bank 中的所有文件，并参考 `progress.md` 了解当前进度，然后继续实施计划的第 2 步。"
-   重复此流程，直至完成整个实施计划。

</details>

</details>

<details>
<summary><strong>✨ 增补功能</strong></summary>

在完成核心功能后，您可以开始进行实验和功能扩展。
-   对于每个主要的新功能，创建一个独立的 `feature-implementation.md`，其中包含简短的步骤和测试方法。
-   继续采用增量式的方式实现和测试。

</details>

<details>
<summary><strong>🐞 故障排查</strong></summary>

<details>
<summary><strong>常规修复</strong></summary>

-   **回滚**: 如果 AI 的某次操作导致问题，使用版本控制工具（如 `git reset`）或 AI 工具自带的回滚命令（如 `/rewind`）恢复到之前的状态。
-   **错误处理**: 将浏览器控制台中的错误信息或问题截图提供给 AI 进行分析。

</details>

<details>
<summary><strong>疑难问题</strong></summary>

-   **重试**: 如果某个问题难以解决，回退到上一个稳定的版本，并尝试用不同的提示词或方法重新实现。
-   **全局上下文**: 在极端情况下，可使用 `RepoPrompt` 等工具将整个代码库打包为一个文件，并提交给 AI 以获得全局性的解决方案。

</details>

</details>

<details>
<summary><strong>💡 提示与技巧</strong></summary>

<details>
<summary><strong>AI 工具使用技巧</strong></summary>

-   **终端集成**: 在 VSCode 终端中运行 AI CLI 工具，可以直接查看文件差异并提供上下文，无需离开工作区。
-   **自定义命令**: 创建自定义快捷命令，以触发特定提示词，从而让模型在修改代码前充分理解上下文。
-   **上下文管理**: 适时使用 `/clear` 或 `/compact` 等命令清理或压缩上下文。
-   **高阶指令**: 通过加入 "请一步一步思考" 或 "ultrathink" 等关键词，引导 AI 进行更深度的思考。

</details>

</details>

<details>
<summary><strong>❓ 常见问题解答 (FAQ)</strong></summary>

-   **Q: 此流程是否适用于非游戏应用开发？**
    -   **A:** 是的，基本流程完全适用。只需将“游戏设计文档”替换为“产品需求文档 (PRD)”即可。

-   **Q: 为何推荐使用原生 CLI 工具而非 Cursor 等集成环境？**
    -   **A:** 这主要取决于个人偏好。我们认为原生 CLI 工具能更好地发挥底层模型的全部实力，并且具有更强的灵活性和可定制性，适用于远程服务器等多种场景。

-   **Q: 我不了解如何搭建服务器，该怎么办？**
    -   **A:** 请咨询您的 AI 助手。

</details>

---

## 📞 联系方式

-   **GitHub**: [tukuaiai](https://github.com/tukuaiai)
-   **Twitter / X**: [123olp](https://x.com/123olp)
-   **Telegram**: [@desci0](https://t.me/desci0)
-   **Telegram 交流群**: [glue_coding](https://t.me/glue_coding)
-   **Telegram 频道**: [tradecat_ai_channel](https://t.me/tradecat_ai_channel)
-   **邮箱**: tukuai.ai@gmail.com (回复可能不及时)

---

## ✨ 支持项目

救救孩子，感谢了，好人一生平安🙏🙏🙏

-   **Tron (TRC20)**: `TQtBXCSTwLFHjBqTS4rNUp7ufiGx51BRey`
-   **Solana**: `HjYhozVf9AQmfv7yv79xSNs6uaEU5oUk2USasYQfUYau`
-   **Ethereum (ERC20)**: `0xa396923a71ee7D9480b346a17dDeEb2c0C287BBC`
-   **BNB Smart Chain (BEP20)**: `0xa396923a71ee7D9480b346a17dDeEb2c0C287BBC`
-   **Bitcoin**: `bc1plslluj3zq3snpnnczplu7ywf37h89dyudqua04pz4txwh8z5z5vsre7nlm`
-   **Sui**: `0xb720c98a48c77f2d49d375932b2867e793029e6337f1562522640e4f84203d2e`
-   **币安 UID**: `572155580`

---

### ✨ 贡献者

感谢所有为本项目做出贡献的开发者！

<a href="https://github.com/tukuaiai/vibe-coding-cn/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tukuaiai/vibe-coding-cn" />
  <img src="https://contrib.rocks/image?repo=EnzeD/vibe-coding" />
</a>

<p>特别鸣谢以下成员的宝贵贡献 (排名不分先后):<br/>
<a href="https://x.com/shao__meng">@shao__meng</a> |
<a href="https://x.com/0XBard_thomas">@0XBard_thomas</a> |
<a href="https://x.com/Pluvio9yte">@Pluvio9yte</a> |
<a href="https://x.com/xDinoDeer">@xDinoDeer</a> |
<a href="https://x.com/geekbb">@geekbb</a>
</p>

---

## 🤝 参与贡献

我们热烈欢迎各种形式的贡献。如果您对本项目有任何想法或建议，请随时开启一个 [Issue](https://github.com/tukuaiai/vibe-coding-cn/issues) 或提交一个 [Pull Request](https://github.com/tukuaiai/vibe-coding-cn/pulls)。

在您开始之前，请花时间阅读我们的 [**贡献指南 (CONTRIBUTING.md)**](CONTRIBUTING.md) 和 [**行为准则 (CODE_OF_CONDUCT.md)**](CODE_OF_CONDUCT.md)。

---

## 📜 许可证

本项目采用 [MIT](LICENSE) 许可证。

---

<div align="center">

**如果这个项目对您有帮助，请考虑为其点亮一颗 Star ⭐！**

## Star History

<a href="https://www.star-history.com/#tukuaiai/vibe-coding-cn&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=tukuaiai/vibe-coding-cn&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=tukuaiai/vibe-coding-cn&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=tukuaiai/vibe-coding-cn&type=date&legend=top-left" />
 </picture>
</a>

---

**由 [tukuaiai](https://github.com/tukuaiai), [Nicolas Zullo](https://x.com/NicolasZu), 和 [123olp](https://x.com/123olp) 倾力打造**

[⬆ 返回顶部](#vibe-coding-指南)
</div>
