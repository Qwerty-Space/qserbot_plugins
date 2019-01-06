"""Responds to "h" with a sticker.  Only from certain users.

pattern: `h+$`
"""

from .global_functions import probability, log
from telethon import events, sync


@events.register(events.NewMessage(pattern="h+$", chats=232787997, outgoing=False))
async def on_h(event):
    await log(event)
    await event.reply(file="CAADAgADxSgAAuCjggcKB413JNAx6wI")
