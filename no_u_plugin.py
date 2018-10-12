r"""Will respond to many variations of "no u" with "no no u", to "no no no u" with "no no no no u" and so on.

pattern:  `(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$`
"""

from telethon import events, sync


@events.register(events.NewMessage(pattern=r"(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$", outgoing=False, fowards=False))
async def no_u(event):
    if event.is_private:
        await event.reply(f"{event.pattern_match.group(1)}{event.pattern_match.string}".lower())
