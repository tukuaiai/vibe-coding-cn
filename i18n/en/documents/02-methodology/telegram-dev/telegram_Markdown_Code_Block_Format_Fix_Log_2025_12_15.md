# Telegram Markdown Code Block Format Fix Log 2025-12-15

## Problem

After completing the astrological chart generation, sending a message reports an error:
```
❌ Chart generation failed: Can't parse entities: can't find end of the entity starting at byte offset 168
```

## Cause

The Markdown code block format for the `header` message in `bot.py` is incorrect.

The original code used string concatenation, adding `\n` after ```, which caused the Telegram Markdown parser to incorrectly identify the code block boundary:

```python
# Incorrect way
header = (
    "```\n"
    f"{filename}\n"
    "```\n"
)
```

## Fix

Changed to a triple-quoted string to ensure ``` is on a separate line:

```python
# Correct way
header = f"""Report attached
```
{filename}
{ai_filename}
```
"""
```

## Modified File

- `services/telegram-service/src/bot.py` lines 293-308

```