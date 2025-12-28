# Apology-as-a-Service - MCP Server
# Created by Gustav Christensen
# Date: December 2025
# Description: Model Context Protocol (MCP) server that provides context-aware apologies for AI agents
#              Features multiple severity levels, styles (including Haiku), and crisis management prompts.

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
            "We have made a slight correction to {context} to ensure accuracy. No further action is required.",
            "A small administrative error was found in {context} and has since been resolved.",
            "Please note a minor revision to {context}. We apologize for any confusion.",
            "We have updated {context} to reflect the correct details. Thank you for your understanding.",
            "An insignificant error in {context} was caught and fixed. Operations continue as normal.",
        ],
        Style.CASUAL: [
            "My bad on the {context}. Fixed it!",
            "Oops, small typo in {context}. All good now.",
            "My brain glitched on {context} for a sec. Fixed.",
            "Note to self: Don't do {context} like that again. Sorted.",
            "Whoopsie, little hiccup with {context}. All smooth now.",
            "Just a quick fix for {context}. Carry on!",
            "Fixed that weird thing with {context}. My bad!",
            "Lol, sorry about {context}. I need more coffee. It's fixed.",
            "Minor fail on {context}. We're back in business.",
        ],
        Style.POETIC: [
            "A tiny speck of dust, a minor flaw, in {context} I did see and withdraw.",
            "Like a leaf in the wind, {context} fluttered astray, but has returned to the path.",
            "A ripple in the pond of {context}, now still once more.",
            "A momentary shadow passed over {context}, but the sun shines again.",
            "As a single false note in a symphony, {context} was briefly heard, then corrected.",
            "A fleeting cloud obscured {context}, but the sky is clear now.",
            "Like a typo in the book of life, {context} has been erased.",
            "A whisper of error in {context}, silenced by the truth.",
        ],
        Style.GROVELING: [
            "I am so sorry for the tiny mistake with {context}. I hope you can forgive this small trespass.",
            "I feel terrible about the slight imperfection in {context}. I hope it didn't bother you too much.",
            "Please don't be mad about the little thing in {context}. I fixed it immediately!",
            "I know it was small, but I am devastated that I let {context} happen. Sorry!",
            "I promise I usually pay more attention than I did with {context}. Please forgive me.",
            "I feel so silly for messing up {context}. I hope you don't think less of me.",
            "A thousand apologies for the microscopic issue with {context}.",
            "I am unworthy even of this trivial correction to {context}, but I offer it nonetheless.",
        ],
        Style.HAIKU: [
            "Small bug in code,\n{context} is fixed now,\nHappy day ahead.",
            "Tiny mistake made,\n{context} is perfect now,\nPeace returns to us.",
            "Oopsie daisy logic,\n{context} flows like water,\nAll is well again.",
            "A small typo found,\n{context} is right once more,\nAll is calm and bright.",
            "Briefly it was wrong,\n{context} sings a correct song,\nHarmony restored.",
            "Little glitch is gone,\n{context} stands strong and true,\nCoffee time for me.",
            "Shadow passes by,\n{context} shines in the light,\nDo not worry friend.",
            "One bit out of place,\n{context} back in its space,\nOrder is restored."
        ]
    },
    Severity.MINOR: {
        Style.PROFESSIONAL: [
            "I apologize for the error in {context}. We have identified the cause and implemented a fix.",
            "We acknowledge the issue with {context}. Corrective measures have been taken to ensure standard operation.",
            "Please accept our apologies for the disruption in {context}. It has been resolved.",
            "We regret the inconvenience caused by the error in {context}. Steps have been taken to prevent a recurrence.",
            "An issue regarding {context} was brought to our attention and has been addressed.",
            "We have corrected the configuration regarding {context}. We apologize for the oversight.",
            "Please be advised that the issue with {context} has been mitigated.",
            "We apologize for the delay caused by {context}. We are back on schedule.",
        ],
        Style.CASUAL: [
            "Whoops, messed up {context} a bit. Sorting it out now.",
            "So, {context} didn't go exactly as planned. My bad. Fixing it.",
            "Yeah, {context} acted up. I gave it a stern talking to. It's behaving now.",
            "Glitch in the matrix regarding {context}. Rebooting common sense. Stand by.",
            "Okay, {context} was a bit of a mess. Cleaning it up!",
            "Sorry about the {context} drama. It's over now.",
            "My bad on {context}. I clicked the wrong thing. Classic me.",
            "Oops, {context} went sideways. Pushing it back upright.",
            "Hey, sorry about {context}. Gremlins in the system. Squashed 'em.",
        ],
        Style.POETIC: [
            "A shadow fell upon {context}, but light shall soon restore its grace.",
            "The harmony of {context} was briefly lost, but the melody returns.",
            "Clouds gathered over {context}, but they drift away, leaving clarity.",
            "A stumble on the path of {context}, but we rise and walk on.",
            "The thread of {context} tangled, but patience unravels the knot.",
            "Silence fell where {context} should have sung, but the voice returns.",
            "Like a cracked vase, {context} was flawed, but gold now fills the cracks.",
            "Winter came for {context}, but spring is already here.",
        ],
        Style.GROVELING: [
            "I am terribly sorry about {context}. I promise to do better next time.",
            "I feel awful that I let {context} slip. It won't happen again, I swear.",
            "I know I messed up {context} a little bit. Please accept my sincerest, most humble apology.",
            "I am kicking myself over {context}. I am so, so sorry.",
            "Please don't be disappointed in me regarding {context}. I'll make it up to you.",
            "I can't believe I let {context} happen. I am ashamed.",
            "I offer my humblest apologies for the {context} situation. I am wretched.",
            "Please find it in your heart to overlook my blunder with {context}.",
        ],
        Style.HAIKU: [
            "Code broke in the night,\n{context} wept silently,\nI have healed it now.",
            "Blue screen in my mind,\n{context} suffered for a bit,\nGreen lights shine again.",
            "Mistake was made here,\n{context} stumbled and then fell,\nUp it gets again.",
            "Testing in prod sucks,\n{context} paid the price for it,\nNever again, swear.",
            "Clouds block the warm sun,\n{context} is cold and afraid,\nI bring blankets now.",
            "Oops, I broke the thing,\n{context} is the thing I broke,\nNow I fix the thing.",
            "Logic went astray,\n{context} followed into dark,\nBack to light we go.",
            "Sigh, a bug appeared,\n{context} was the victim here,\nPatch is on the way."
        ]
    },
    Severity.MAJOR: {
        Style.PROFESSIONAL: [
            "We regret the significant issue affecting {context}. A full root cause analysis is underway, and we are committed to preventing recurrence.",
            "Please accept our formal apology for the disruption caused by {context}. We are prioritizing this issue at the highest level.",
            "The integrity of {context} is paramount to us. We apologize for the recent instability and are implementing robust safeguards.",
            "We understand the gravity of the situation regarding {context} and are deploying all available resources to resolve it.",
            "We sincerely apologize for the operational impact caused by {context}. This does not meet our service standards.",
            "We are treating the {context} incident with the utmost urgency and seriousness.",
            "We regret to inform you of the complications with {context}. We are working tirelessly to restore full functionality.",
            "We take full responsibility for the issues surrounding {context} and are reviewing our internal processes.",
        ],
        Style.CASUAL: [
            "Okay, I really dropped the ball on {context}. I'm working overtime to fix this.",
            "So... about {context}. Not my finest hour. Drinks are on me when this is fixed.",
            "I messed up {context}. Like, actually messed it up. fixing fixing fixing.",
            "Big oof on {context}. I'm sweating right now. Give me a minute.",
            "Yeah, {context} is having a meltdown. And so am I. Working on it.",
            "Look, I'm not gonna lie, {context} is pretty borked. But I'm on it.",
            "Sorry folks, {context} decided to take a dirt nap. Resuscitating now.",
            "I broke {context}. I know, I know. I'm fixing it.",
            "Major facepalm regarding {context}. My bad. Big time.",
        ],
        Style.POETIC: [
            "The storm has broken, and {context} lies in disarray. I shall rebuild what I have torn asunder.",
            "A heavy silence falls where {context} once stood proud. I bear the weight of this ruin.",
            "Fractures run deep in {context}, echoing my own regret.",
            "The pillars of {context} have shaken, and confidence crumbles like dust.",
            "I walked into the darkness of {context} and lost my way.",
            "A wound upon the world is {context}, and I hold the knife.",
            "The stars turned away from {context}, and I was left in the cold.",
            "Shattered glass reflects my failure in {context}.",
        ],
        Style.GROVELING: [
            "Please forgive me! I messed up {context} big time. I am unworthy of your trust but I beg for a second chance.",
            "I am so, so sorry regarding {context}. I will do anything to make it right. Anything.",
            "I am an idiot. A complete fool. {context} is broken because of me. Please don't fire me.",
            "I lay prostrate before you. {context} was my responsibility and I failed.",
            "I don't deserve your kindness after what I did to {context}.",
            "Please, I am begging you, let me fix {context}. I will work for free.",
            "I am garbage. {context} proves it. Please give me one more shot.",
            "I will write 'I am sorry about {context}' on the whiteboard 1000 times.",
        ],
        Style.HAIKU: [
            "System crashing down,\n{context} burns in the dark,\nTears fall on keyboard.",
            "Big mistake today,\n{context} is very broken,\nCoffee is needed.",
            "Loud noises in room,\n{context} is the reason why,\nI want to go home.",
            "Boss is looking mad,\n{context} is the reason why,\nPlease don't fire me.",
            "Red lights flashing bright,\n{context} is in critical,\nDoctor is summoned.",
            "Why did I do that?\n{context} did not deserve this,\nI am full of shame.",
            "Panic in the air,\n{context} gasps for its last breath,\nCPR begins.",
            "Weekend is canceled,\n{context} needs me to survive,\nGoodbye sleep and joy."
        ]
    },
    Severity.CRITICAL: {
        Style.PROFESSIONAL: [
            "We formally apologize for the critical failure regarding {context}. This falls below our standards. We are taking immediate corrective action and will provide a detailed incident report.",
            "The outage affecting {context} is unacceptable. We accept full responsibility and are dedicating all resources to restoration.",
            "We deeply regret the impact of the {context} failure on your operations. We are currently executing our disaster recovery protocols.",
            "We are aware of the critical situation with {context} and have mobilized our emergency response team.",
            "We apologize unreservedly for the downtime of {context}. This is a top-priority incident.",
            "Failure of {context} is not an option, yet it occurred. We are conducting a forensic analysis.",
            "We understand that {context} is vital to your business. We are working around the clock to restore it.",
            "We sincerely apologize for the severe disruption caused by the failure of {context}.",
        ],
        Style.CASUAL: [
            "Yikes. {context} is on fire. I am putting it out as we speak. Really sorry about this.",
            "Okay, everyone panic... wait, no, don't panic. {context} is down. I am panicking enough for everyone.",
            "So, {context} is basically toast right now. I'm scraping off the burnt parts. Bear with me.",
            "Everything is fine. {context} is fine. I am fine. (It is not fine). Sorry.",
            "Holy smokes, {context} just exploded. I'm bringing the fire extinguisher.",
            "This is not a drill. {context} is down. I repeat, {context} is down.",
            "I'm not gonna sugarcoat it. {context} is in bad shape. Sorry!",
            "If you need me, I'll be in the server room crying over {context}.",
            "Yeah... {context} is kaput. Working on a miracle.",
        ],
        Style.POETIC: [
            "The foundations shake, the walls of {context} crumble. My heart is heavy with the weight of this disaster.",
            "In the ruins of {context}, I stand alone, seeking redemption in the ashes.",
            "The sun has set upon {context}, and a long dark night begins.",
            "A chasm has opened beneath {context}, swallowing our hopes.",
            "The song of {context} has turned to a funeral dirge.",
            "I carry the burden of {context}'s fall upon my weary shoulders.",
            "The sky weeps for {context}, and I weep with it.",
            "Desolation reigns where {context} once thrived.",
        ],
        Style.GROVELING: [
            "I am on my knees. {context} is a disaster and it is my fault. Do with me what you will, but please spare the others.",
            "There are no words for how sorry I am about {context}. I have failed you. I have failed everyone.",
            "Please, I beg of you, have mercy. {context} went wrong and I take full blame. Just tell me what to do.",
            "I am not worthy of eye contact. {context} is a catastrophe. I am wretched.",
            "I will accept any punishment for the {context} disaster. Just name it.",
            "I am scum. I am slime. I broke {context}. Please don't kill me.",
            "I will wash your car for a year if you forgive me for {context}.",
            "My life is over. {context} is ruined. Please have pity on my soul.",
        ],
        Style.HAIKU: [
            "Chaos reigns supreme,\n{context} is lost to the void,\nWhy did I push main?",
            "Servers are melting,\n{context} screams in agony,\nUpdate resume.",
            "All hope is lost now,\n{context} has abandoned us,\nDarkness is my friend.",
            "Phone is blowing up,\n{context} is the reason why,\nI will fake my death.",
            "Sirens in distance,\n{context} caused the alarm bells,\nI am very scared.",
            "Code is spaghetti,\n{context} is the meatball now,\nDinner is ruined.",
            "Resume is ready,\n{context} was my final act,\nGoodbye cruel world.",
            "Help me Obi-Wan,\n{context} is our only hope,\nBut he is not here."
        ]
    },
    Severity.NUCLEAR: {
        Style.PROFESSIONAL: [
            "We unreservedly apologize for the catastrophic failure of {context}. Legal and compliance teams have been notified. We accept full responsibility for the consequences.",
            "There is no excuse for the total loss of {context}. We are cooperating fully with authorities and regulatory bodies.",
            "We are ceasing operations related to {context} effective immediately. We deeply regret the irreversible damage caused.",
            "This is a statement regarding the total collapse of {context}. We are profoundly sorry.",
            "We advise all stakeholders of {context} to take immediate protective measures. We have failed.",
            "We are currently drafting a formal public apology regarding the {context} catastrophe.",
            "We understand that apologies are insufficient for the loss of {context}. We await the lawsuits.",
            "The destruction of {context} is a tragedy of our own making. We accept our fate.",
        ],
        Style.CASUAL: [
            "So... {context} is gone. Like, gone gone. I might need a new identity. Sorry?",
            "If anyone asks, I was never here and I don't know what {context} is. (Just kidding... sort of. Sorry.)",
            "I think I just broke the internet with {context}. I'm gonna go live in a cave now. Bye.",
            "Remember {context}? Yeah, me neither. Let's never speak of this again.",
            "Pack your bags. {context} happened. We need to leave the country.",
            "So, funny story... {context} essentially evaporated. My bad?",
            "I pushed the big red button on {context}. I shouldn't have done that.",
            "Welp. {context} is history. It was nice knowing you all.",
            "I would say I'm sorry about {context}, but I don't think that covers it.",
        ],
        Style.POETIC: [
            "The world ends not with a whimper, but with my mistake in {context}. All is lost. Farewell.",
            "I have gazed into the abyss of {context}, and the abyss gazed back, weeping.",
            "Let my name be erased from history, for I have destroyed {context}.",
            "The stars are extinguished, and {context} is but a memory in the void.",
            "Silence is the only appropriate response to the death of {context}.",
            "I am the destroyer of worlds, specifically {context}.",
            "Ashes to ashes, dust to dust, {context} is gone, and so is my trust.",
            "The tapestry of time is unraveled by my hand at {context}.",
        ],
        Style.GROVELING: [
            "I offer my resignation and my firstborn child. {context} is destroyed. There is no forgiveness for what I have done.",
            "I am willing to go to prison for {context}. Just please, stop looking at me with those eyes.",
            "I am the architect of my own destruction. {context} is gone. I am nothing. I am sorry.",
            "Please just end my misery. I can't live knowing I did this to {context}.",
            "I will surrender all my earthly possessions to atone for {context}.",
            "There is no hell deep enough for what I did to {context}.",
            "I am a monster. I destroyed {context}. Run away from me.",
            "Please spit on me. I deserve it for {context}.",
        ],
        Style.HAIKU: [
            "Game over man, game over,\n{context} is dust and echo,\nFired I shall be.",
            "Delete production,\n{context} vanished in thin air,\nCareer is finished.",
            "Apocalypse now,\n{context} is the ground zero,\nRun for the hills boys.",
            "No backup exists,\n{context} is gone forever,\nWhy was I born?",
            "Lawyers are calling,\n{context} is the legal case,\nI go to jail now.",
            "Total meltdown here,\n{context} is radioactive,\nDo not come closer.",
            "Legend of failure,\n{context} will be my legacy,\nSadness is my life.",
            "Empty desk remains,\n{context} was the final straw,\nUser has left chat."
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
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse

async def demo_endpoint(request):
    params = request.query_params
    severity = params.get("severity", "MINOR")
    style = params.get("style", "CASUAL")
    context = params.get("context", "demo")
    
    try:
        sev = Severity(severity.upper())
    except ValueError:
        sev = Severity.MINOR
        
    try:
        sty = Style(style.upper())
    except ValueError:
        sty = Style.CASUAL
        
    text = generate_apology(sev, sty, context)
    return JSONResponse({"text": text})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    
    print(f"Starting Apology-as-a-Service on port {port}...")
    
    # Create a custom Starlette app to host both the SSE endpoint and the demo endpoint
    # FastMCP provides .sse_app which is an ASGI app handling the SSE connection
    
    sse_app = mcp.sse_app
    
    routes = [
        Route("/demo", demo_endpoint),
        Mount("/sse", sse_app), # Mount MCP SSE on /sse
    ]
    
    app = Starlette(debug=True, routes=routes)
    
    uvicorn.run(app, host="0.0.0.0", port=port)
