import global_functions
from telethon import events, sync


async def foobar(event):
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
    if event.from_id == 232787997:
        return
    await event.reply("^bar$")

foobar.event = events.NewMessage(pattern="foo", chats=1001040270887, outgoing=False)