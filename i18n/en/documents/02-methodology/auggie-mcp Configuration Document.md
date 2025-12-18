# auggie-mcp Detailed Configuration Document

## Installation Steps

### 1. Install Auggie CLI
```bash
npm install -g @augmentcode/auggie@prerelease
```

### 2. User Authentication
```bash
# Method 1: Interactive login
auggie login

# Method 2: Use token (suitable for CI/CD)
export AUGMENT_API_TOKEN="your-token"
export AUGMENT_API_URL="https://i0.api.augmentcode.com/"
```

## Claude Code Configuration

### Add to User Configuration (Global)
```bash
claude mcp add-json auggie-mcp --scope user '{
  "type": "stdio",
  "command": "auggie",
  "args": ["--mcp"],
  "env": {
    "AUGMENT_API_TOKEN": "your-token",
    "AUGMENT_API_URL": "https://i0.api.augmentcode.com/"
  }
}'
```

### Add to Project Configuration (Current Project)
```bash
claude mcp add-json auggie-mcp --scope project '{
  "type": "stdio",
  "command": "auggie",
  "args": ["-w", "/path/to/project", "--mcp"],
  "env": {
    "AUGMENT_API_TOKEN": "your-token",
    "AUGMENT_API_URL": "https://i0.api.augmentcode.com/"
  }
}'
```

## Codex Configuration

Edit `~/.codex/config.toml`:
```toml
[mcp_servers."auggie-mcp"]
command = "auggie"
args = ["-w", "/path/to/project", "--mcp"]
startup_timeout_ms = 20000
```

## Verify Installation

```bash
# Check MCP status
claude mcp list

# Should display:
# auggie-mcp: auggie --mcp - ✓ Connected

# Test functionality
claude --print "Use codebase-retrieval to search all files in the current directory"
```

## Tool Usage Examples

### 1. Search Specific Files
```bash
# Search all Python files
claude --print "Use codebase-retrieval to search *.py files"

# Search specific directory
claude --print "Use codebase-retrieval to search files in src/ directory"
```

### 2. Code Analysis
```bash
# Analyze function implementation
claude --print "Use codebase-retrieval to find the implementation of the main function"

# Search API endpoints
claude --print "Use codebase-retrieval to search all API endpoint definitions"
```

## Environment Variable Configuration

Create `~/.augment/config` file:
```json
{
  "apiToken": "your-token",
  "apiUrl": "https://i0.api.augmentcode.com/",
  "defaultModel": "gpt-4",
  "workspaceRoot": "/path/to/project"
}
```

## Troubleshooting

### 1. Connection Failure
```bash
# Check token
auggie token print

# Re-login
auggie logout && auggie login
```

### 2. Path Error
```bash
# Use absolute path
auggie -w $(pwd) --mcp

# Check if path exists
ls -la /path/to/project
```

### 3. Permission Issues
```bash
# Check file permissions
ls -la ~/.augment/

# Fix permissions
chmod 600 ~/.augment/session.json
```

## Advanced Configuration

### Custom Cache Directory
```bash
export AUGMENT_CACHE_DIR="/custom/cache/path"
```

### Set Retry Timeout
```bash
export AUGMENT_RETRY_TIMEOUT=30
```

### Disable Confirmation Prompt
```bash
auggie --allow-indexing --mcp
```
