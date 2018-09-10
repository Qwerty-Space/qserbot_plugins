import re
from telethon import events, sync
from global_functions import probability

async def no_u(event):
    if event.is_private:
        await event.reply(f"no {event.pattern_match.string}".lower())

no_u.event = events.NewMessage(pattern=re.compile(r"(no ){1,50}(u|you)$", re.I).match, outgoing=False)
