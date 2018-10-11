"""The bot will edit a message with the time it took to respond to your command.
Only responds to the person running the script.

pattern:  `/uping$`
"""

from datetime import datetime
from telethon import events, sync
from .global_functions import probability


# /ping
@events.register(events.NewMessage(pattern=r"/uping$", incoming=False))
async def ping_pong(event):
    sender = await event.get_sender()
    a = datetime.timestamp(datetime.now())
    await event.edit("**Pong!**")
    b = datetime.timestamp(datetime.now()) - a
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string} [{b:.3f}]")
    await event.edit(f"**Pong!**\nTook `{b:.3f}` seconds")
