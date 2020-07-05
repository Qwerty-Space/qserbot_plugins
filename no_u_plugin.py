r"""Will respond to many variations of "no u" with "no no u", to "no no no u" with "no no no no u" and so on.

pattern:  `(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$`
"""

from .global_functions import log
from telethon import events, sync

@events.register(events.NewMessage(
        pattern=r"(?i)(n(o|ein|ada)+[\s\u2063]+){1,50}([bdj]?(?:[uü]+|y\s?(?:o\s?u|e\s?w)))", 
        outgoing=False, forwards=False)
        )
async def no_u(event):
    if not event.is_private:
        return

    await event.reply(f"{event.pattern_match.group(1)}{event.pattern_match.string}".lower())
    await log(event)
