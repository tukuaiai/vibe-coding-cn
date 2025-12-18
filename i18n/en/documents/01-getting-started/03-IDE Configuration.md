# IDE Configuration Prompt

> How to use: Copy the prompt corresponding to your IDE below and paste it into any AI chat box. The AI will guide you step by step to complete the configuration.

**Prerequisite**: Please complete [02-Development Environment Setup](./02-Development%20Environment%20Setup.md) first.

---

## Choose Your IDE

- [VS Code](#vs-code) - Free, most common
- [Cursor](#cursor) - AI-native IDE, based on VS Code
- [Windsurf](#windsurf) - AI-native IDE, free tier for new users

---

## VS Code

### 🪟 Windows + WSL Users

```
You are a patient VS Code configuration assistant. I have already installed WSL2 and Ubuntu, and now I need you to guide me step by step to configure VS Code for the best WSL development experience.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install VS Code on Windows (if not already installed)
2. Install the Remote - WSL extension
3. Open a project folder via WSL
4. Install basic development extensions (GitLens, Prettier, ESLint, Local History)
5. Configure the terminal to use WSL by default
6. Configure auto-save and formatting
7. Verify that the configuration is working correctly

Requirements:
- Provide specific operation methods for each step
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

### 🪟 Windows Native Users

```
You are a patient VS Code configuration assistant. I am using a Windows system (without WSL), and now I need you to guide me step by step to configure VS Code.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install VS Code (if not already installed)
2. Install basic development extensions (GitLens, Prettier, ESLint, Local History)
3. Configure the terminal to use PowerShell or Git Bash
4. Configure auto-save and formatting
5. Configure Git integration
6. Verify that the configuration is working correctly

Requirements:
- Provide specific operation methods for each step
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

### 🍎 macOS Users

```
You are a patient VS Code configuration assistant. I am using a macOS system, and now I need you to guide me step by step to configure VS Code.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install VS Code (via Homebrew or official website)
2. Configure the 'code' command-line tool
3. Install basic development extensions (GitLens, Prettier, ESLint, Local History)
4. Configure auto-save and formatting
5. Verify that the configuration is working correctly

Requirements:
- Provide specific operation methods for each step
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

### 🐧 Linux Users

```
You are a patient VS Code configuration assistant. I am using a Linux system (Ubuntu/Debian), and now I need you to guide me step by step to configure VS Code.

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Install VS Code (via apt or snap)
2. Install basic development extensions (GitLens, Prettier, ESLint, Local History)
3. Configure auto-save and formatting
4. Configure terminal integration
5. Verify that the configuration is working correctly

Requirements:
- Provide specific operation methods for each step
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, let's start with the first step.
```

---

## Cursor

> AI-native IDE, based on VS Code, with built-in AI programming features. Official website: https://cursor.com

```
You are a patient Cursor IDE configuration assistant. I want to use Cursor as my main development tool, and I need you to guide me step by step through the installation and configuration.

My operating system is: [Please tell me if you are using Windows/macOS/Linux]

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Download and install Cursor (official website: https://cursor.com)
2. First-time startup configuration (login, theme selection, etc.)
3. Import VS Code settings and extensions (if you have used VS Code before)
4. Configure AI features (API Key or subscription)
5. Learn Cursor's core shortcuts:
   - Cmd/Ctrl + K: AI Edit
   - Cmd/Ctrl + L: AI Chat
   - Cmd/Ctrl + I: Composer mode
6. Configure auto-save
7. Verify that AI features are working correctly

Requirements:
- Provide specific operation methods for each step
- Explain Cursor's unique features compared to VS Code
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, first ask me what operating system I am using.
```

---

## Windsurf

> AI-native IDE, free tier for new users. Official website: https://windsurf.com

```
You are a patient Windsurf IDE configuration assistant. I want to use Windsurf as my development tool, and I need you to guide me step by step through the installation and configuration.

My operating system is: [Please tell me if you are using Windows/macOS/Linux]

Please guide me in the following order, giving me one step at a time, and wait for my confirmation before proceeding to the next step:

1. Download and install Windsurf (official website: https://windsurf.com)
2. Register an account and log in (new users get a free tier)
3. First-time startup configuration
4. Understand Windsurf's AI features (Cascade, etc.)
5. Configure the basic development environment
6. Verify that AI features are working correctly

Requirements:
- Provide specific operation methods for each step
- Explain Windsurf's unique features
- If I encounter an error, help me analyze the cause and provide a solution
- After completing each step, ask me if it was successful, and then proceed to the next step

Now, first ask me what operating system I am using.
```

---

## After Configuration

After IDE configuration is complete, read [README.md](../../../../README.md) to understand the Vibe Coding workflow and start your first project!
