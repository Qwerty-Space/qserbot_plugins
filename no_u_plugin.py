r"""Will respond to many variations of "no u" with "no no u", to "no no no u" with "no no no no u" and so on.

pattern:  `(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$`
"""

from telethon import events, sync


@events.register(events.NewMessage(pattern=r"(?i)(n\w+h? ){1,50}(\w?(?:[uü]+|y(?:ou|ew)))$", outgoing=False, fowards=False))
async def no_u(event):
    me = await event.client.get_me()
    if event.is_reply:
        replied_to = (await event.get_reply_message()).from_id
    else:
        try: 
            prev_id = (event.id) - 1
            replied_to = (await event.client.get_messages(event.chat_id, ids=prev_id)).from_id
        except AttributeError:
            replied_to = None
    if event.is_private or replied_to == me.id:
        await event.reply(f"{event.pattern_match.group(1)}{event.pattern_match.string}".lower())
        sender = await event.get_sender()
        print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
