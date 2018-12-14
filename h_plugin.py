"""Responds to "h" with a sticker.  Only in private.

pattern:  `h+$`
"""

from .global_functions import probability
from telethon import events, sync


@events.register(events.NewMessage(pattern="h+$", outgoing=False))
async def on_h(event):
    if event.is_private:
        sender = await event.get_sender()
        print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
        await event.reply(file="CAADBAAD2QUAAk9YoFB_ajbmDNP3kgI")
