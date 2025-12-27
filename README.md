# Apology-as-a-Service (AaaS)

**"Because sometimes, 'my bad' just isn't enough."**

This is a Model Context Protocol (MCP) server that provides highly sophisticated, context-aware apologies for AI agents. Whether you broke the build, forgot an anniversary, or accidentally deleted the production database, AaaS has you covered.

## Features

- **Severity Levels:**
  - `TRIVIAL`: For minor inconveniences (e.g., "typo in comment").
  - `MINOR`: For noticeable errors (e.g., "broke the dev build").
  - `MAJOR`: For significant issues (e.g., "missed a deadline").
  - `CRITICAL`: For career-limiting moves (e.g., "dropped prod table").
  - `NUCLEAR`: For existential threats (e.g., "leaked all user data").

- **Styles:**
  - `PROFESSIONAL`: Corporate speak.
  - `CASUAL`: "My bad, bro".
  - `POETIC`: Shakespearean regret.
  - `GROVELING`: Begging for forgiveness.

## Usage

### Prerequisite
- Python 3.10+
- `uv` (recommended) or `pip`

### Installation

```bash
uv sync
# or
pip install -e .
```

### Run with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "apology-service": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/Apology-as-a-Service",
        "run",
        "mcp-server-apology"
      ]
    }
  }
}
```
