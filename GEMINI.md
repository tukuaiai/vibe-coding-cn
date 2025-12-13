# GEMINI.md - 项目上下文文档 (Project Context Document)

## 项目概述 (Project Overview)

`vibe-coding-cn` 项目旨在提供一个通过与 AI 结对编程实现“将想法变为现实”的终极工作流程。它强调“规划驱动”和“模块化”的核心理念，旨在避免 AI 失控导致的项目混乱。该项目不仅仅是一个代码库，更是一个全面的 AI 结对编程指南、庞大的提示词库和模块化的技能工具集，涵盖了从项目构思、技术选型、实施规划到具体开发、调试和扩展的全过程。

**核心理念:** 规划是核心，通过结构化、模块化的方式引导 AI，确保项目可控、可维护。

## 技术栈 (Technology Stack)

本项目主要的技术栈和相关工具包括：

*   **核心语言:** Python (用于 `prompts-library` 工具和备份脚本)
*   **CLI 交互:** `rich`, `InquirerPy` (用于 `prompts-library` 提供友好的命令行界面)
*   **数据处理:** `pandas`, `openpyxl` (用于 `prompts-library` 处理 Excel 文件)
*   **配置管理:** `PyYAML` (用于 `prompts-library` 的配置)
*   **文档规范:** `markdownlint-cli` (用于 `Makefile` 中的 `lint` 任务)
*   **版本控制:** Git
*   **自动化:** Makefile
*   **操作系统:** 兼容 Linux

## 主要功能与工作流程 (Key Features & Workflow)

1.  **AI 提示词库 (`prompts/`):**
    *   一个极其庞大和精细分类的提示词集合，是项目的核心资产。
    *   `coding_prompts/`: 专注于编程和代码生成的提示词。
    *   `system_prompts/`: 用于设定 AI 行为和思维框架的系统级提示词。
    *   `user_prompts/`: 用户自定义或常用的提示词。

2.  **提示词库管理工具 (`prompts/prompts-library/`):**
    *   提供 Python 工具 (`main.py`)，用于在 Excel 工作簿 (`prompt_excel/`) 和 Markdown 文档 (`prompt_docs/`) 之间进行提示词的相互转换。
    *   支持交互式和非交互式操作。

3.  **技能库 (`skills/`):**
    *   一个模块化的技能集合，为 AI 提供了特定工具和领域的知识。
    *   每个技能（如 `ccxt`, `postgresql`, `telegram-dev`）都包含独立的 `SKILL.md` 描述、参考资料和脚本。

4.  **项目备份工具 (`backups/`):**
    *   `快速备份.py` 脚本能根据 `.gitignore` 规则智能地打包项目文件为 `.tar.gz` 格式。

5.  **知识库与文档 (`documents/`):**
    *   包含代码组织、开发经验、系统提示词构建原则、项目架构模板等各类文档。

## 文件结构 (File Structure)

```
.
├── AGENTS.md                    # 面向 AI Agent 的贡献与行为准则。
├── CLAUDE.md                    # 面向 Claude 模型的上下文与指令。
├── GEMINI.md                    # 面向 Gemini 模型的上下文与指令 (本文档)。
├── README.md                    # 项目主文档，包含项目概览、使用指南等。
├── Makefile                     # 项目自动化脚本 (lint, backup 等)。
│
├── backups/                     # 项目备份脚本。
│   ├── 一键备份.sh
│   └── 快速备份.py
│
├── documents/                   # 存放各类说明文档、经验总结和配置。
│
├── libs/                        # 通用库代码 (当前为骨架)。
│   ├── common/
│   ├── database/
│   └── external/
│
├── prompts/                     # 核心资产：AI 提示词库。
│   ├── coding_prompts/          # 编程与代码生成相关提示词。
│   ├── prompts-library/         # 提示词库管理工具 (Excel-Markdown 互转)。
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── prompt_excel/
│   │   └── prompt_docs/
│   ├── system_prompts/          # AI 系统级提示词。
│   └── user_prompts/            # 用户自定义提示词。
│
└── skills/                      # 模块化技能库。
    ├── ccxt/                    # CCXT 加密货币交易库技能。
    ├── claude-code-guide/       # Claude Code 使用指南技能。
    ├── postgresql/              # PostgreSQL 数据库技能。
    ├── telegram-dev/            # Telegram Bot 开发技能。
    └── ... (其他 10+ 个技能)
```