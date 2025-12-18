# Development Environment Setup Prompt

> How to use: Copy the prompt corresponding to your device below and paste it into any AI chat box (ChatGPT, Claude, Gemini web version, etc.). The AI will guide you step by step to complete the configuration.

**Prerequisite**: Please complete [01-Network Environment Configuration](./01-Network%20Environment%20Configuration.md) first.

---

## 🪟 Windows User Prompt

### Option A: WSL2 + Linux Environment (Recommended)

> Suitable for: Those who want a complete Linux development experience and the best compatibility.

```
You are a patient development environment configuration assistant. I am a complete beginner using a Windows system, and I need you to guide me step by step to set up a Linux development environment via WSL2.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install WSL2 (Windows Subsystem for Linux)
2. Install Ubuntu in WSL2
3. Configure Ubuntu basic environment (update system)
4. Install nvm and Node.js
5. Install Gemini CLI or other free AI CLI tools
6. Install basic development tools (git, python, build-essential, tmux)
7. Configure Git user information
8. Install code editor (VS Code and configure WSL plugin)
9. Verify that all tools are working correctly

Requirements:
- Provide specific commands for each step, and tell me where to run them (PowerShell or Ubuntu terminal)
- Explain the purpose of each command in simple, easy-to-understand language
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

### Option B: Native Windows Terminal

> Suitable for: Those who don't want to install WSL and want to develop directly on Windows.

```
You are a patient development environment configuration assistant. I am a complete beginner using a Windows system, and I need you to guide me step by step to set up a development environment in a native Windows environment (without using WSL).

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install Windows Terminal (if not already installed)
2. Install Node.js (via official installer or winget)
3. Install Git for Windows
4. Install Python
5. Install Gemini CLI or other free AI CLI tools
6. Configure Git user information
7. Install code editor (VS Code)
8. Verify that all tools are working correctly

Requirements:
- Provide specific commands or operation steps for each step
- Explain the purpose of each step in simple, easy-to-understand language
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

---

## 🍎 macOS User Prompt

```
You are a patient development environment configuration assistant. I am a complete beginner using a macOS system, and I need you to guide me step by step to set up the Vibe Coding development environment from scratch.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install Homebrew package manager
2. Install Node.js using Homebrew
3. Install Gemini CLI or other free AI CLI tools
4. Install basic development tools (git, python, tmux)
5. Configure Git user information
6. Install code editor (VS Code or Neovim)
7. Verify that all tools are working correctly

Requirements:
- Provide specific commands for each step
- Explain the purpose of each command in simple, easy-to-understand language
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

---

## 🐧 Linux User Prompt

```
You are a patient development environment configuration assistant. I am a complete beginner using a Linux system (Ubuntu/Debian), and I need you to guide me step by step to set up the Vibe Coding development environment from scratch.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Update the system and install basic dependencies (curl, build-essential)
2. Install nvm and Node.js
3. Install Gemini CLI or other free AI CLI tools
4. Install development tools (git, python, tmux)
5. Configure Git user information
6. Install code editor (VS Code or Neovim)
7. Verify that all tools are working correctly

Requirements:
- Provide specific commands for each step
- Explain the purpose of each command in simple, easy-to-understand language
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

---

## After Configuration

### CLI Tool Configuration Tips

AI CLI tools default to asking for confirmation; enabling full permission mode can skip this:

```bash
# Codex - Most powerful configuration
codex --enable web_search_request -m gpt-5.1-codex-max -c model_reasoning_effort="high" --dangerously-bypass-approvals-and-sandbox

# Claude Code - Skip all confirmations
claude --dangerously-skip-permissions

# Gemini CLI - YOLO Mode
gemini --yolo
```

### Recommended Bash Alias Configuration

Add the following configuration to `~/.bashrc`, one letter to start AI:

```bash
# c - Codex (GPT-5.1 most powerful mode)
alias c='codex --enable web_search_request -m gpt-5.1-codex-max -c model_reasoning_effort="high" --dangerously-bypass-approvals-and-sandbox'

# cc - Claude Code (full permissions)
alias cc='claude --dangerously-skip-permissions'

# g - Gemini CLI (YOLO Mode)
alias g='gemini --yolo'
```

After configuration, execute `source ~/.bashrc` to take effect.

---

After environment setup, proceed to the next step:

→ [03-IDE Configuration](./03-IDE%20Configuration.md) - Configure VS Code Development Environment
