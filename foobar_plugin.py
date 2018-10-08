"""Responds to "bar" with "foo" in progtech
"""

from .global_functions import probability
from telethon import events, sync


@events.register(events.NewMessage(pattern="foo", chats=1001040270887, outgoing=False))
async def foobar(event):
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
    if event.from_id == 232787997:
        return
    await event.reply("^bar$")
