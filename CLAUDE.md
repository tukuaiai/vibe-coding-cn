# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Vibe Coding CN** repository - a comprehensive guide and toolset for AI-assisted programming workflows. The project focuses on:
- Systematic prompt engineering for AI coding assistants
- Excel ↔ Markdown conversion tools for prompt management
- Documentation and best practices for vibe coding methodology

## Key Commands

### Prompt Library Management
```bash
# Convert Excel prompts to Markdown documentation
cd prompts/prompts-library
python3 main.py

# Non-interactive conversion
python3 main.py --select "prompt_excel/prompt.xlsx"
python3 main.py --select "prompt_docs/prompt_docs_2025_1213_080256"
```

### Development & Maintenance
```bash
# Lint markdown files
make lint

# Backup project (respects .gitignore)
bash backups/一键备份.sh
# or directly
python3 backups/快速备份.py

# Install dependencies for prompt library
cd prompts/prompts-library
pip install -r requirements.txt
```

## Architecture & Structure

### Core Directories
- **`prompts/`** - All AI prompts organized by type
  - `coding_prompts/` - Development workflow prompts
  - `system_prompts/` - AI behavior configuration (CLAUDE.md variants 1-10)
  - `prompts-library/` - Excel↔Markdown conversion tool
  - `user_prompts/` - User-contributed prompts

- **`documents/`** - Knowledge base and methodology docs
  - Contains development principles, architecture templates, and experience summaries

- **`libs/`** - Modular code libraries (Python-based)
  - `common/` - Shared utilities and models
  - `database/` - Database integration modules
  - `external/` - Third-party integrations

- **`backups/`** - Project backup utilities
  - Automated backup with .gitignore compliance

### Key Technical Details

1. **Prompt Organization**: Prompts use `(r,c)_` prefix notation for categorization (row,column matrix system)

2. **Conversion Tool**: The prompts-library uses pandas + openpyxl for Excel operations, supports bidirectional conversion with rich CLI interface

3. **System Prompts**: Multiple CLAUDE.md variants (1-10) represent different AI behavior configurations, with version 10 being the latest comprehensive version incorporating augment context engine requirements

4. **Documentation Standards**: All user-facing documentation in Chinese, code/structure in English

## Development Workflow

When modifying this repository:
1. Follow the existing prompt categorization system
2. Update both Excel and Markdown versions when modifying prompts
3. Use the conversion tool to maintain consistency
4. Run backups before major changes
5. Follow the Chinese(文档)/English(代码) language separation

## Important Notes

- This is a documentation and tooling repository, not a runtime application
- The Makefile commands are mostly placeholders - actual functionality is in Python scripts
- Prompt management is the core functionality - always use the conversion tools to maintain consistency
- The repository serves as a knowledge base for vibe coding best practices