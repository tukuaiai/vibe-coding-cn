# CLAUDE.md

This file provides guidance to Claude series models when working with code in this repository.

## Repository Overview

This is the **Vibe Coding CN** repository, a workflow, toolset, and knowledge base for advanced AI-assisted programming. The project's core assets are its extensive `prompts` and `skills` libraries.

## Key Commands

### Prompt Library Management
```bash
# Enter the library directory
cd prompts/prompts-library

# Run the interactive conversion tool
python3 main.py
```

### Development & Maintenance
```bash
# Lint all markdown files in the repository
make lint

# Create a full project backup (respects .gitignore)
bash backups/一键备份.sh
```

## Architecture & Structure

### Core Directories
- **`prompts/`**: The core asset. A massive, well-organized library of prompts.
  - `coding_prompts/`, `system_prompts/`, `user_prompts/`
- **`skills/`**: A modular library of skills for the AI, providing domain-specific knowledge for various tools like `ccxt`, `postgresql`, `telegram-dev`, etc.
- **`documents/`**: The project's knowledge base, containing methodology, principles, and guides.
- **`prompts/prompts-library/`**: A Python-based tool for converting prompts between Excel and Markdown formats.
- **`backups/`**: Scripts for project backups.
- **`libs/`**: Skeleton for shared Python library code.

### Key Technical Details
1.  **Prompt Organization**: Prompts use a `(row,col)_` prefix for categorization.
2.  **Conversion Tool**: The `prompts-library` uses Python with `pandas` and `openpyxl`.
3.  **Documentation Standard**: User-facing documentation is in Chinese. Code, file names, and structure are in English.
4.  **Skills**: The `skills` directory provides context and knowledge for specific tools and domains, each with its own `SKILL.md`.

## Development Workflow

When modifying this repository:
1.  Follow the existing prompt and skill categorization systems.
2.  Use the `prompts-library` tool to maintain consistency when updating prompts.
3.  Run `make lint` after changing any Markdown files.
4.  Run a backup with `bash backups/一键备份.sh` before any major refactoring.