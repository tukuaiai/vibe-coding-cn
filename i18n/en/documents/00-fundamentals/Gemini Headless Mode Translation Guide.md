# Gemini Headless Mode Translation Guide

Objective: To perform non-interactive bulk translation locally using Gemini CLI (gemini-2.5-flash), avoiding tool calls and permission pop-ups, suitable for quick machine translation drafts of prompts/skills/documents.

## Principle Overview
-   CLI connects directly to Gemini API using locally cached Google credentials; model inference is done in the cloud.
-   Use `--allowed-tools ''` to disable tool calls, ensuring only plain text is returned, without triggering shell/browser actions.
-   Pass text to be translated via standard input, and get results from standard output, facilitating script pipeline processing.
-   A proxy (http/https) can be set to route requests through a local proxy node, improving success rate and stability.

## Basic Commands
```bash
# Proxy (if needed)
export http_proxy=http://127.0.0.1:9910
export https_proxy=http://127.0.0.1:9910

# Single example: Chinese -> English
printf '你好，翻译成英文。' | gemini -m gemini-2.5-flash \
  --output-format text \
  --allowed-tools '' \
  "Translate this to English."
```
-   The prompt can be placed as a positional argument (`-p/--prompt` is deprecated).
-   Output is plain text, can be redirected for saving.

## Batch File Translation Example (stdin → stdout)
```bash
src=i18n/zh/prompts/README.md
dst=i18n/en/prompts/README.md
cat "$src" | gemini -m gemini-2.5-flash --output-format text --allowed-tools '' \
  "Translate to English; keep code fences unchanged." > "$dst"
```
-   Can loop through multiple files in a script; check exit code and output on failure.

## Integration with existing l10n-tool
-   l10n-tool (deep-translator) is used for full machine translation; if quality or connectivity is unstable, it can be switched to file-by-file processing with Gemini CLI.
-   Process: `cat source_file | gemini ... > target_file`; if necessary, place redirection instructions or manually proofread in other language directories.

## Notes
-   Ensure `gemini` command is in PATH and identity authentication is complete (first run will guide login).
-   For long texts, it is recommended to split them into segments to avoid timeouts; code blocks can be kept as is by declaring "keep code fences unchanged" in the prompt.
-   Adjust proxy port according to actual environment; if no proxy is needed, omit relevant environment variables.
