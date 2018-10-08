"""Responds to "h" with a sticker.  Only from certain users.

pattern: `h+$`
"""

from .global_functions import probability
from telethon import events, sync


@events.register(events.NewMessage(pattern="h+$", chats=232787997, outgoing=False))
async def on_h(event):
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
    await event.reply(file="CAADAgADxSgAAuCjggcKB413JNAx6wI")
