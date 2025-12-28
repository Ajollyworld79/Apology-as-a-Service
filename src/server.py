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
    HAIKU = "HAIKU"

TEMPLATES = {
    Severity.TRIVIAL: {
        Style.PROFESSIONAL: [
            "Please accept my apologies for the minor oversight regarding {context}. It has been promptly corrected.",
            "I noticed a small discrepancy in {context} and have rectified it. Thank you for your patience.",
            "Regarding {context}, a minor adjustment was required and has been applied. We apologize for the notification.",
        ],
        Style.CASUAL: [
            "My bad on the {context}. Fixed it!",
            "Oops, small typo in {context}. All good now.",
            "My brain glitched on {context} for a sec. Fixed.",
            "Note to self: Don't do {context} like that again. Sorted.",
        ],
        Style.POETIC: [
            "A tiny speck of dust, a minor flaw, in {context} I did see and withdraw.",
            "Like a leaf in the wind, {context} fluttered astray, but has returned to the path.",
            "A ripple in the pond of {context}, now still once more.",
        ],
        Style.GROVELING: [
            "I am so sorry for the tiny mistake with {context}. I hope you can forgive this small trespass.",
            "I feel terrible about the slight imperfection in {context}. I hope it didn't bother you too much.",
            "Please don't be mad about the little thing in {context}. I fixed it immediately!",
        ],
        Style.HAIKU: [
            "Small bug in code,\n{context} is fixed now,\nHappy day ahead.",
            "Tiny mistake made,\n{context} is perfect now,\nPeace returns to us.",
            "Oopsie daisy logic,\n{context} flows like water,\nAll is well again."
        ]
    },
    Severity.MINOR: {
        Style.PROFESSIONAL: [
            "I apologize for the error in {context}. We have identified the cause and implemented a fix.",
            "We acknowledge the issue with {context}. Corrective measures have been taken to ensure standard operation.",
            "Please accept our apologies for the disruption in {context}. It has been resolved.",
        ],
        Style.CASUAL: [
            "Whoops, messed up {context} a bit. Sorting it out now.",
            "So, {context} didn't go exactly as planned. My bad. Fixing it.",
            "Yeah, {context} acted up. I gave it a stern talking to. It's behaving now.",
            "Glitch in the matrix regarding {context}. Rebooting common sense. Stand by.",
        ],
        Style.POETIC: [
            "A shadow fell upon {context}, but light shall soon restore its grace.",
            "The harmony of {context} was briefly lost, but the melody returns.",
            "Clouds gathered over {context}, but they drift away, leaving clarity.",
        ],
        Style.GROVELING: [
            "I am terribly sorry about {context}. I promise to do better next time.",
            "I feel awful that I let {context} slip. It won't happen again, I swear.",
            "I know I messed up {context} a little bit. Please accept my sincerest, most humble apology.",
        ],
        Style.HAIKU: [
            "Code broke in the night,\n{context} wept silently,\nI have healed it now.",
            "Blue screen in my mind,\n{context} suffered for a bit,\nGreen lights shine again."
        ]
    },
    Severity.MAJOR: {
        Style.PROFESSIONAL: [
            "We regret the significant issue affecting {context}. A full root cause analysis is underway, and we are committed to preventing recurrence.",
            "Please accept our formal apology for the disruption caused by {context}. We are prioritizing this issue at the highest level.",
            "The integrity of {context} is paramount to us. We apologize for the recent instability and are implementing robust safeguards.",
        ],
        Style.CASUAL: [
            "Okay, I really dropped the ball on {context}. I'm working overtime to fix this.",
            "So... about {context}. Not my finest hour. Drinks are on me when this is fixed.",
            "I messed up {context}. Like, actually messed it up. fixing fixing fixing.",
            "Big oof on {context}. I'm sweating right now. Give me a minute.",
        ],
        Style.POETIC: [
            "The storm has broken, and {context} lies in disarray. I shall rebuild what I have torn asunder.",
            "A heavy silence falls where {context} once stood proud. I bear the weight of this ruin.",
            "Fractures run deep in {context}, echoing my own regret.",
        ],
        Style.GROVELING: [
            "Please forgive me! I messed up {context} big time. I am unworthy of your trust but I beg for a second chance.",
            "I am so, so sorry regarding {context}. I will do anything to make it right. Anything.",
            "I am an idiot. A complete fool. {context} is broken because of me. Please don't fire me.",
        ],
        Style.HAIKU: [
            "System crashing down,\n{context} burns in the dark,\nTears fall on keyboard.",
            "Big mistake today,\n{context} is very broken,\nCoffee is needed."
        ]
    },
    Severity.CRITICAL: {
        Style.PROFESSIONAL: [
            "We formally apologize for the critical failure regarding {context}. This falls below our standards. We are taking immediate corrective action and will provide a detailed incident report.",
            "The outage affecting {context} is unacceptable. We accept full responsibility and are dedicating all resources to restoration.",
            "We deeply regret the impact of the {context} failure on your operations. We are currently executing our disaster recovery protocols.",
        ],
        Style.CASUAL: [
            "Yikes. {context} is on fire. I am putting it out as we speak. Really sorry about this.",
            "Okay, everyone panic... wait, no, don't panic. {context} is down. I am panicking enough for everyone.",
            "So, {context} is basically toast right now. I'm scraping off the burnt parts. Bear with me.",
            "Everything is fine. {context} is fine. I am fine. (It is not fine). Sorry.",
        ],
        Style.POETIC: [
            "The foundations shake, the walls of {context} crumble. My heart is heavy with the weight of this disaster.",
            "In the ruins of {context}, I stand alone, seeking redemption in the ashes.",
            "The sun has set upon {context}, and a long dark night begins.",
        ],
        Style.GROVELING: [
            "I am on my knees. {context} is a disaster and it is my fault. Do with me what you will, but please spare the others.",
            "There are no words for how sorry I am about {context}. I have failed you. I have failed everyone.",
            "Please, I beg of you, have mercy. {context} went wrong and I take full blame. Just tell me what to do.",
        ],
        Style.HAIKU: [
            "Chaos reigns supreme,\n{context} is lost to the void,\nWhy did I push main?",
            "Servers are melting,\n{context} screams in agony,\nUpdate resume."
        ]
    },
    Severity.NUCLEAR: {
        Style.PROFESSIONAL: [
            "We unreservedly apologize for the catastrophic failure of {context}. Legal and compliance teams have been notified. We accept full responsibility for the consequences.",
            "There is no excuse for the total loss of {context}. We are cooperating fully with authorities and regulatory bodies.",
            "We are ceasing operations related to {context} effective immediately. We deeply regret the irreversible damage caused.",
        ],
        Style.CASUAL: [
            "So... {context} is gone. Like, gone gone. I might need a new identity. Sorry?",
            "If anyone asks, I was never here and I don't know what {context} is. (Just kidding... sort of. Sorry.)",
            "I think I just broke the internet with {context}. I'm gonna go live in a cave now. Bye.",
            "Remember {context}? Yeah, me neither. Let's never speak of this again.",
        ],
        Style.POETIC: [
            "The world ends not with a whimper, but with my mistake in {context}. All is lost. Farewell.",
            "I have gazed into the abyss of {context}, and the abyss gazed back, weeping.",
            "Let my name be erased from history, for I have destroyed {context}.",
        ],
        Style.GROVELING: [
            "I offer my resignation and my firstborn child. {context} is destroyed. There is no forgiveness for what I have done.",
            "I am willing to go to prison for {context}. Just please, stop looking at me with those eyes.",
            "I am the architect of my own destruction. {context} is gone. I am nothing. I am sorry.",
        ],
        Style.HAIKU: [
            "Game over man, game over,\n{context} is dust and echo,\nFired I shall be.",
            "Delete production,\n{context} vanished in thin air,\nCareer is finished."
        ]
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
    # Pick a random template from the list
    templates_list = TEMPLATES[severity][style]
    base_msg = random.choice(templates_list).format(context=context)
    
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
