"""Start message

Makes people stfu about my new profile pic in PM
"""

from telethon import client, events
from .global_functions import log
from fuzzywuzzy import fuzz
import re


# Fuzzy checcks the message
def fuzzyfinder(msg, pfp):
    if fuzz.partial_ratio(f"you changed your {pfp}", msg) >= 80:
        return True

    if fuzz.partial_ratio(f"you got a new {pfp}", msg) >= 80:
        return True

    if fuzz.partial_ratio(f"you have a new {pfp}", msg) >= 80:
        return True
    
    return False


# hi
@events.register(events.NewMessage(pattern=re.compile(r"(?i)\b((pf|p(rofile)?|display|dp) ?(p(ic(ture)?|ima?ge?)?)?\b)").search, incoming=True))
async def on_pfp(event):
    if event.is_private:    # If command was sent in private
        msg = event.pattern_match.string
        pfp = event.pattern_match.group(1)
        fuzzyfinder(msg, pfp)

        await log(event, msg)    # Logs the event
        await event.delete()
