# Apology-as-a-Service - MCP Server
# Created by Gustav Christensen
# Description: Model Context Protocol (MCP) server that provides context-aware apologies
#              for AI agents. Multiple severity levels, styles, crisis prompts, plus
#              tooling to grade and escalate apologies. Supports both Streamable HTTP
#              (current MCP transport) and SSE (legacy) for backward compatibility.

import contextlib
import os
import random
import re

import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import BaseRoute, Route

from .templates import TEMPLATES, Severity, Style

mcp = FastMCP("Apology-as-a-Service")


def _render(severity: Severity, style: Style, context: str, recipient: str) -> str:
    base_msg = random.choice(TEMPLATES[severity][style]).format(context=context)
    return f"Dear {recipient},\n\n{base_msg}\n\nSincerely,\n[Your Name]"


@mcp.tool()
def generate_apology(
    severity: Severity,
    style: Style,
    context: str,
    recipient: str = "Client",
) -> str:
    """
    Generates a context-aware apology based on severity and style.

    Args:
        severity: How bad did you mess up? (TRIVIAL to NUCLEAR)
        style: The tone of the apology. Includes PROFESSIONAL, CASUAL, POETIC,
               GROVELING, HAIKU, LEGAL_DISCLAIMER, CORPORATE_DOUBLESPEAK,
               SHAKESPEAREAN, PIRATE.
        context: What specifically went wrong? (e.g. "the production database",
                 "your wedding anniversary")
        recipient: Who are we apologizing to?
    """
    return _render(severity, style, context, recipient)


@mcp.tool()
def escalation_ladder(
    context: str,
    style: Style = Style.PROFESSIONAL,
    recipient: str = "Client",
) -> dict:
    """
    Returns one apology at every severity level in the given style. Useful when
    you want to pick the right level of remorse for the situation.

    Args:
        context: What went wrong.
        style: Tone to use across all severities (default PROFESSIONAL).
        recipient: Who you are apologizing to.
    """
    return {
        severity.value: _render(severity, style, context, recipient)
        for severity in Severity
    }


_SINCERITY_WORDS = (
    "sorry",
    "apolog",
    "regret",
    "fault",
    "responsib",
    "mistake",
    "wrong",
    "forgive",
)
_GROVEL_WORDS = (
    "beg",
    "worthless",
    "unworthy",
    "wretched",
    "please",
    "garbage",
    "scum",
    "monster",
    "knees",
    "mercy",
    "prostrate",
    "spit",
)
_HEDGE_WORDS = (
    "without admitting",
    "without prejudice",
    "no admission",
    "reserving",
    "disclaim",
    "notwithstanding",
    "pursuant",
    "alleged",
    "if any",
    "to the extent",
)


def _count_hits(text: str, needles) -> int:
    lowered = text.lower()
    return sum(lowered.count(n) for n in needles)


@mcp.tool()
def rate_my_apology(text: str) -> dict:
    """
    Grades an apology on sincerity, cringe, and hedging. Returns scores 0-10
    plus a one-line verdict. Heuristic only — for entertainment.

    Args:
        text: The apology text to evaluate.
    """
    if not text or not text.strip():
        return {
            "sincerity": 0,
            "cringe": 0,
            "hedging": 0,
            "word_count": 0,
            "verdict": "Empty apology. The silent treatment, but worse.",
        }

    word_count = len(re.findall(r"\b\w+\b", text))
    sincerity_hits = _count_hits(text, _SINCERITY_WORDS)
    grovel_hits = _count_hits(text, _GROVEL_WORDS)
    hedge_hits = _count_hits(text, _HEDGE_WORDS)

    # Normalize to 0-10. Density per 50 words, capped.
    density = max(word_count / 50, 1)
    sincerity = min(round(sincerity_hits / density * 3), 10)
    cringe = min(round(grovel_hits / density * 4), 10)
    hedging = min(round(hedge_hits / density * 5), 10)

    if hedging >= 6:
        verdict = "Your lawyer wrote this. Nobody is fooled."
    elif cringe >= 7:
        verdict = "Dial it back. This reads like a hostage video."
    elif sincerity >= 6 and cringe <= 4 and hedging <= 3:
        verdict = "Solid. Owns the mistake without melodrama."
    elif sincerity <= 2:
        verdict = "This is not an apology. This is a press release."
    elif cringe >= 4 and sincerity >= 4:
        verdict = "Sincere but a touch theatrical. Trim the grovel."
    else:
        verdict = "Passable. Will not move mountains, but will not start fires."

    return {
        "sincerity": sincerity,
        "cringe": cringe,
        "hedging": hedging,
        "word_count": word_count,
        "verdict": verdict,
    }


@mcp.prompt()
def save_my_ass(incident_description: str) -> str:
    """
    Helps you save your rear end when things are really burning.
    Generates a complete crisis communication plan.
    """
    return f"""
    I need help handling the following crisis: "{incident_description}"

    Please generate 3 options for apologies:
    1. A 'Safe/Professional' one (if I want to keep my job)
    2. An 'Honest/Human' one (if I know them well)
    3. A 'Groveling/Desperate' one (if I am about to be fired)

    For each option, explain why it works and what the risk is.
    """


# --- SERVER CONFIGURATION ---

_ROOT_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Apology-as-a-Service</title>
  <style>
    body { font-family: -apple-system, system-ui, sans-serif; max-width: 720px;
           margin: 4rem auto; padding: 0 1.5rem; color: #222; line-height: 1.5; }
    code { background: #f3f3f3; padding: 0.15rem 0.35rem; border-radius: 4px; }
    h1 { margin-bottom: 0.25rem; }
    .sub { color: #666; margin-top: 0; }
    ul { padding-left: 1.25rem; }
    li { margin-bottom: 0.4rem; }
  </style>
</head>
<body>
  <h1>Apology-as-a-Service</h1>
  <p class="sub"><em>Because sometimes, "my bad" just isn't enough.</em></p>

  <h2>Endpoints</h2>
  <ul>
    <li><code>GET /health</code> &mdash; liveness check</li>
    <li><code>GET /demo?severity=CRITICAL&amp;style=HAIKU&amp;context=prod+db</code>
        &mdash; quick HTTP demo</li>
    <li><code>/mcp</code> &mdash; MCP Streamable HTTP transport (current)</li>
    <li><code>/sse</code> &mdash; MCP SSE transport (legacy, kept for old clients)</li>
  </ul>

  <h2>Source</h2>
  <p>
    <a href="https://github.com/Ajollyworld79/Apology-as-a-Service">GitHub</a>
  </p>
</body>
</html>"""


async def root_endpoint(request):
    return HTMLResponse(_ROOT_HTML)


async def health_endpoint(request):
    return JSONResponse({"status": "ok", "service": "Apology-as-a-Service"})


async def demo_endpoint(request):
    params = request.query_params
    severity_raw = params.get("severity", "MINOR")
    style_raw = params.get("style", "CASUAL")
    context = params.get("context", "demo")
    recipient = params.get("recipient", "Client")

    # Clamp context length so the demo endpoint can't be abused as a megaphone.
    context = context[:500]
    recipient = recipient[:100]

    try:
        sev = Severity(severity_raw.upper())
    except ValueError:
        sev = Severity.MINOR

    try:
        sty = Style(style_raw.upper())
    except ValueError:
        sty = Style.CASUAL

    return JSONResponse({"text": _render(sev, sty, context, recipient)})


def _build_app() -> Starlette:
    # The transport sub-apps already serve at /mcp, /sse and /messages internally,
    # so their routes are merged into the top-level app instead of being mounted
    # under a prefix (mounting would have produced /mcp/mcp and /sse/sse).
    streamable_app = mcp.streamable_http_app()
    sse_app = mcp.sse_app()

    routes: list[BaseRoute] = [
        Route("/", root_endpoint),
        Route("/health", health_endpoint),
        Route("/demo", demo_endpoint),
        *streamable_app.routes,
        *sse_app.routes,
    ]

    # The Streamable HTTP session manager only works while its run() context is
    # active. Starlette does not run lifespans of sub-apps, so it is wired into
    # the top-level app's lifespan here.
    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette):
        async with mcp.session_manager.run():
            yield

    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            # DELETE is used by Streamable HTTP clients to terminate sessions.
            allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
            allow_headers=["*"],
            # Browser clients must be able to read the session id header.
            expose_headers=["Mcp-Session-Id"],
        ),
    ]

    return Starlette(
        debug=False, routes=routes, middleware=middleware, lifespan=lifespan
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting Apology-as-a-Service on port {port}...")
    uvicorn.run(_build_app(), host="0.0.0.0", port=port)
