r"""Will respond to many variations of "no u" with "no no u", to "no no no u" with "no no no no u" and so on.

pattern:  `(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$`
"""

import re
from telethon import events, sync
from .global_functions import probability

@events.register(events.NewMessage(pattern=re.compile(r"(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$", re.I).match, outgoing=False))
async def no_u(event):
    if event.is_private:
        await event.reply(f"{event.pattern_match.group(1)}{event.pattern_match.string}".lower())
