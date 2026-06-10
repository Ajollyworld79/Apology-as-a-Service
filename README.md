# Apology-as-a-Service (AaaS)

> *"Because sometimes, 'my bad' just isn't enough."*

🟢 **Live endpoints:**

- Streamable HTTP (current MCP): `https://apology-as-a-service-production.up.railway.app/mcp`
- SSE (legacy, kept for older clients): `https://apology-as-a-service-production.up.railway.app/sse`
- Quick HTTP demo: `https://apology-as-a-service-production.up.railway.app/demo`

A Model Context Protocol (MCP) server that provides highly sophisticated, context-aware apologies for AI agents. Whether you broke the build, forgot an anniversary, or accidentally deleted the production database, AaaS has you covered.

## Features

### Tools

#### `generate_apology(severity, style, context, recipient="Client")`

The original. Generates the perfect apology for any situation.

#### Severity Levels

- `TRIVIAL` — minor inconveniences ("typo in comment")
- `MINOR` — noticeable errors ("broke the dev build")
- `MAJOR` — significant issues ("missed a deadline")
- `CRITICAL` — career-limiting moves ("dropped prod table")
- `NUCLEAR` — existential threats ("leaked all user data")

#### Styles

- `PROFESSIONAL` — corporate speak for the modern enterprise
- `CASUAL` — "my bad, bro" energy for Slack threads
- `POETIC` — Shakespearean regret for the dramatic soul
- `GROVELING` — begging for forgiveness when you *really* messed up
- `HAIKU` — 5-7-5 syllables of pure remorse
- `LEGAL_DISCLAIMER` — *"without admitting fault or liability..."*
- `CORPORATE_DOUBLESPEAK` — *"mistakes were made, learnings have been captured"*
- `SHAKESPEAREAN` — *"Et tu, prod database? Then fall, mine career."*
- `PIRATE` — *"Arrr, the database be at the bottom of Davy Jones' locker."*
- `PASSIVE_AGGRESSIVE` — *"Sorry about the outage. I flagged this risk three weeks ago, but sure, let's all act surprised."*
- `GEN_Z` — *"the prod db is cooked and it's my fault. locking in, do not perceive me."*
- `VIKING` — *"Ragnarök has come early for the database, and I am the one who loosed the wolf."*
- `ROBOT` — *"ERROR: backups not found. ERROR: dignity not found. Apology: found, and offered at maximum amplitude."*
- `EXISTENTIAL` — *"Nietzsche warned me about the abyss. He never mentioned it had a DROP TABLE statement."*
- `SOAP_OPERA` — *"It wasn't a hacker. It wasn't bad luck. It was me, the trusted one, all along."*

#### `escalation_ladder(context, style="PROFESSIONAL", recipient="Client")`

Returns one apology at *every* severity level in the given style. Useful when you're not sure how badly to apologize — calibrate by reading them side by side.

#### `rate_my_apology(text)`

Grades any apology on three axes: **sincerity**, **cringe**, and **hedging** (each 0–10), plus a one-line verdict. Heuristic only — for entertainment.

### Prompts

#### `save_my_ass(incident_description)`

Generates a complete crisis communication plan with three options (Safe, Honest, Desperate) including risk assessment for each.

## HTTP endpoints

| Path     | Purpose                                                     |
|----------|-------------------------------------------------------------|
| `/`      | Landing page with endpoint list                             |
| `/health`| JSON liveness check (`{"status": "ok"}`)                    |
| `/demo`  | Plain HTTP wrapper around `generate_apology` (query params) |
| `/mcp`   | MCP **Streamable HTTP** transport (current spec)            |
| `/sse`   | MCP **SSE** transport (legacy, kept for older clients)      |

CORS is open on all routes so the `/demo` endpoint can be called from a browser.

## Usage

### Local development

```bash
pip install -r requirements.txt
python -m src.server
```

### Client configuration

Claude Desktop / Claude Code (remote MCP via Streamable HTTP):

```json
{
  "mcpServers": {
    "apology-service": {
      "url": "https://apology-as-a-service-production.up.railway.app/mcp"
    }
  }
}
```

Older clients that only speak SSE can point at `/sse` instead.

### Deployment (Railway / Docker)

A `Dockerfile` and `.dockerignore` are included. Push to a repo connected to Railway; the server listens on `$PORT` (default 8000).

## Example prompts

- **"I just accidentally deleted the production database. Generate a haiku apology."**
  → `generate_apology(severity=CRITICAL, style=HAIKU, context="the production database")`

- **"Give me the full escalation ladder for missing the demo, in pirate."**
  → `escalation_ladder(context="missing the demo", style=PIRATE)`

- **"Rate this apology I drafted: 'Sorry I guess. Things happen.'"**
  → `rate_my_apology(text="Sorry I guess. Things happen.")`

- **"I forgot my anniversary. Help me save my marriage!"**
  → `save_my_ass(incident_description="forgot anniversary")`

## Example output

**Input:** `severity="CRITICAL", style="SHAKESPEAREAN", context="the main database"`

**Output:**

> Dear Client,
>
> By heavens above, the main database is undone! What tragic deed have mine own hands wrought!
>
> Sincerely,
> [Your Name]

---

Created by Gustav Christensen — December 2025
