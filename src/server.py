from mcp.server.fastmcp import FastMCP
from enum import Enum
import random

# Initialize the MCP Server
mcp = FastMCP("Apology-as-a-Service")

class Severity(str, Enum):
    TRIVIAL = "TRIVIAL"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"
    NUCLEAR = "NUCLEAR"

class Style(str, Enum):
    PROFESSIONAL = "PROFESSIONAL"
    CASUAL = "CASUAL"
    POETIC = "POETIC"
    GROVELING = "GROVELING"

TEMPLATES = {
    Severity.TRIVIAL: {
        Style.PROFESSIONAL: "Please accept my apologies for the minor oversight regarding {context}. It has been corrected.",
        Style.CASUAL: "My bad on the {context}. Fixed it!",
        Style.POETIC: "A tiny speck of dust, a minor flaw, in {context} I did see and withdraw.",
        Style.GROVELING: "I am so sorry for the tiny mistake with {context}. I hope you can forgive this small trespass."
    },
    Severity.MINOR: {
        Style.PROFESSIONAL: "I apologize for the error in {context}. We have identified the cause and implemented a fix.",
        Style.CASUAL: "Whoops, messed up {context} a bit. Sorting it out now.",
        Style.POETIC: "A shadow fell upon {context}, but light shall soon restore its grace.",
        Style.GROVELING: "I am terribly sorry about {context}. I promise to do better next time."
    },
    Severity.MAJOR: {
        Style.PROFESSIONAL: "We regret the significant issue affecting {context}. A full root cause analysis is underway, and we are committed to preventing recurrence.",
        Style.CASUAL: "Okay, I really dropped the ball on {context}. I'm working overtime to fix this.",
        Style.POETIC: "The storm has broken, and {context} lies in disarray. I shall rebuild what I have torn asunder.",
        Style.GROVELING: "Please forgive me! I messed up {context} big time. I am unworthy of your trust but I beg for a second chance."
    },
    Severity.CRITICAL: {
        Style.PROFESSIONAL: "We formally apologize for the critical failure regarding {context}. This falls below our standards. We are taking immediate corrective action and will provide a detailed incident report.",
        Style.CASUAL: "Yikes. {context} is on fire. I am putting it out as we speak. Really sorry about this.",
        Style.POETIC: "The foundations shake, the walls of {context} crumble. My heart is heavy with the weight of this disaster.",
        Style.GROVELING: "I am on my knees. {context} is a disaster and it is my fault. Do with me what you will, but please spare the others."
    },
    Severity.NUCLEAR: {
        Style.PROFESSIONAL: "We unreservedly apologize for the catastrophic failure of {context}. Legal and compliance teams have been notified. We accept full responsibility for the consequences.",
        Style.CASUAL: "So... {context} is gone. Like, gone gone. I might need a new identity. Sorry?",
        Style.POETIC: "The world ends not with a whimper, but with my mistake in {context}. All is lost. Farewell.",
        Style.GROVELING: "I offer my resignation and my firstborn child. {context} is destroyed. There is no forgiveness for what I have done."
    }
}

@mcp.tool()
def generate_apology(severity: Severity, style: Style, context: str, recipient: str = "Client") -> str:
    """
    Generates a context-aware apology based on severity and style.
    
    Args:
        severity: How bad did you mess up? (TRIVIAL to NUCLEAR)
        style: The tone of the apology.
        context: What specifically went wrong? (e.g. "the production database", "your wedding anniversary")
        recipient: Who are we apologizing to?
    """
    base_msg = TEMPLATES[severity][style].format(context=context)
    
    prefix = f"Dear {recipient},\n\n"
    suffix = "\n\nSincerely,\n[Your Name]"
    
    return prefix + base_msg + suffix

@mcp.prompt()
def red_min_røv(incident_description: str) -> str:
    """
    Hjælper dig med at redde din røv når det virkelig brænder på.
    Genererer en komplet krise-kommunikationsplan.
    """
    return f"""
    Jeg har brug for hjælp til at håndtere følgende krise: "{incident_description}"
    
    Vær venlig at generere 3 muligheder for undskyldninger:
    1. En 'Sikker/Professionel' (hvis jeg vil beholde jobbet)
    2. En 'Ærlig/Menneskelig' (hvis jeg kender dem godt)
    3. En 'Groveling/Desperat' (hvis jeg er lige ved at blive fyret)
    
    For hver mulighed, forklar hvorfor den virker, og hvad risikoen er.
    """

if __name__ == "__main__":
    mcp.run()
