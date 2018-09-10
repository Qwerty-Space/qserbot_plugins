import global_functions
from telethon import events, sync


async def on_h(event):
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
    await event.reply(file="CAADAgADxSgAAuCjggcKB413JNAx6wI")

on_h.event = events.NewMessage(pattern="h$", chats=232787997, outgoing=False)
