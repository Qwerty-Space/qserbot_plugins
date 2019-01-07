"""The bot will edit a message with the time it took to respond to your command.

pattern:  `/uping$`
"""

from datetime import datetime
from telethon import events, sync
from .global_functions import probability, log

# /ping
@events.register(events.NewMessage(pattern=r"/uping$", incoming=False))
async def ping_pong(event):
    a = datetime.timestamp(datetime.now())
    await event.edit("**Pong!**")
    b = datetime.timestamp(datetime.now()) - a
    await log(event, f"{b:.3f}")
    await event.edit(f"**Pong!**\nTook `{b:.3f}` seconds")
