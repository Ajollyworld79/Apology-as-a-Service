# Apology-as-a-Service (AaaS)

**"Because sometimes, 'my bad' just isn't enough."**

This is a Model Context Protocol (MCP) server that provides highly sophisticated, context-aware apologies for AI agents. Whether you broke the build, forgot an anniversary, or accidentally deleted the production database, AaaS has you covered.

Now with **Server-Sent Events (SSE)** support for easy deployment!

## Features

### 1. The Apology Generator
Generate the perfect apology for any situation using the `generate_apology` tool.

**Severity Levels:**
- `TRIVIAL`: For minor inconveniences (e.g., "typo in comment").
- `MINOR`: For noticeable errors (e.g., "broke the dev build").
- `MAJOR`: For significant issues (e.g., "missed a deadline").
- `CRITICAL`: For career-limiting moves (e.g., "dropped prod table").
- `NUCLEAR`: For existential threats (e.g., "leaked all user data").

**Styles:**
- `PROFESSIONAL`: Corporate speak for the modern enterprise.
- `CASUAL`: "My bad, bro" energy for Slack threads.
- `POETIC`: Shakespearean regret for the dramatic soul.
- `GROVELING`: Begging for forgiveness when you *really* messed up.
- `HAIKU`: 5-7-5 syllables of pure remorse.

### 2. Crisis Management
Use the `save_my_ass` prompt when you don't even know where to start.
- Takes an incident description.
- Returns 3 actionable options: Safe, Honest, and Desperate.
- Includes risk assessment for each option.

## Usage

### Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python -m src.server
   ```

### Client Configuration (Claude Desktop)
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "apology-service": {
      "command": "python",
      "args": [
        "-m",
        "src.server"
      ],
      "env": {
        "PORT": "8000"
      }
    }
  }
}
```

### Deployment (Railway / Docker)
This server is configured to run via **SSE (Server-Sent Events)** when deployed, making it compatible with remote MCP clients.

1. **Dockerfile** is included.
2. Just push to a repo connected to Railway.
3. It listens on port 8000 (or `$PORT`).

## How to trigger it (Example Prompts)
Once connected to an agent (like Claude), you can simply describe your predicament:

- **"I just accidentally deleted the production database. Generate a haiku apology."**
  -> *Triggers: severity=CRITICAL, style=HAIKU*

- **"I'm late for the meeting because my cat was sleeping on my lap. Make it sound professional."**
  -> *Triggers: severity=MINOR, style=PROFESSIONAL*

- **"I forgot my anniversary. Help me save my marriage!"**
  -> *Triggers: save_my_ass(incident="forgot anniversary")*

## Examples

**Input (Tool Call):**
`severity="CRITICAL", style="HAIKU", context="deleted the main database"`

**Output:**
> Chaos reigns supreme,
> deleted the main database is lost to the void,
> Why did I push main?

---
*Created by Gustav Christensen - December 2025*
