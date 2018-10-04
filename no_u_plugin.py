import re
from telethon import events, sync
from global_functions import probability

async def no_u(event):
    if event.is_private:
        await event.reply(f"{event.pattern_match.group(1)}{event.pattern_match.string}".lower())

no_u.event = events.NewMessage(pattern=re.compile(r"(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$", re.I).match, outgoing=False)
