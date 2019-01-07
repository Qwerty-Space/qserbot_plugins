"""Responds to "h" with a sticker.  Only from certain users.

pattern: `h+$`
"""

from telethon import events
from .global_functions import probability, log


@events.register(events.NewMessage(pattern="h+$", outgoing=False))
async def on_h(event):
    if event.is_private:
        await log(event)
        await event.reply(file="CAADAgADxSgAAuCjggcKB413JNAx6wI")
