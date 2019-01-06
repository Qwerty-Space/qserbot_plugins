"""Responds to "bar" with "foo" in progtech
"""

from .global_functions import probability, log
from telethon import events, sync


@events.register(events.NewMessage(pattern="foo", chats=1001040270887, outgoing=False))
async def foobar(event):
    await log(event)
    if event.from_id == 232787997:
        return
    await event.reply("^bar$")
