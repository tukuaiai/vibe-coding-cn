# telegram Markdown Code Block Format Fix Log 2025-12-15

## Problem

Error when sending message after chart generation:
```
❌ Chart generation failed: Can't parse entities: can't find end of the entity starting at byte offset 168
```

## Cause

The Markdown code block format in the `header` message in `bot.py` is incorrect.

The original code used string concatenation, adding `\n` after ```, which prevented the Telegram Markdown parser from correctly recognizing the code block boundary:

```python
# Incorrect usage
header = (
    "```\n"
    f"{filename}\n"
    "```\n"
)
```

## Fix

Changed to use triple-quoted strings, ensuring ``` is on its own line:

```python
# Correct usage
header = f"""Report in attachment
```
{filename}
{ai_filename}
```
"""
```

## Modified File

- `services/telegram-service/src/bot.py` lines 293-308

