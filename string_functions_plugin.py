r"""A collection of functions to manipulate text (by reply, or in a message):

Most should be obvious as to what they do, but `.vc` will make text 【 ａ ｅ ｓ ｔ ｈ ｅ ｔ ｉ ｃ 】
For example `.vc` by reply, or `(text).vc` to transform specific text.

patterns:
`(?s)(.+)?\.capitali[zs]e$`
`(?s)(.+)?\.lower$`
`(?s)(.+)?\.randcase$`
`(?s)(.+)?\.swapcase$`
`(?s)(.+)?\.title$`
`(?s)(.+)?\.upper$`
`(?s)(.+ )?(?:\((.+)\))?\.vc(.+)?$`
"""

from telethon import events, sync
from random import choice
import re


### STRING METHODS ###
async def string_map(event, string_mapper):
    message_text = event.pattern_match.group(1) or (await event.get_reply_message()).raw_text
    new_message_text = string_mapper(message_text)
    await event.respond(new_message_text, reply_to=event.reply_to_msg_id)
    await event.delete()
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.capitali[zs]e$", incoming=False))
async def capitalize(event):
    await string_map(event, str.capitalize)


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.lower$", incoming=False))
async def lower(event):
    await string_map(event, str.lower)


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.randcase$", incoming=False))
async def randcase(event):
    await string_map(event, lambda x: ''.join(choice([str.upper, str.lower])(c) for c in x))


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.swapcase$", incoming=False))
async def swapcase(event):
    await string_map(event, str.swapcase)


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.title$", incoming=False))
async def title(event):
    await string_map(event, str.title)


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.upper$", incoming=False))
async def upper(event):
    await string_map(event, str.upper)


@events.register(events.NewMessage(pattern=r"(?s)(.+)?\.ladder$", incoming=False))
async def ladder(event):
    def ladderify(text):
        return text.replace(" ", "\n")
    await string_map(event, ladderify)


# 【  Ｖ  Ａ  Ｐ  Ｏ  Ｒ  Ｗ  Ａ  Ｖ  Ｅ  】
# Make string from vaporcase 【  ａ  ｅ  ｓ  ｔ  ｈ  ｅ  ｔ  ｉ  ｃ  】
def vaporwave(message):
    for char in message:
        if char == " ":
            value = 0xFEFF
        elif 0xFF01 <= ord(char) <= 0xFFEF:
            value = ord(char)
        else:
            value = ord(char) + 0xFEE0
        yield chr(value)

# Make message 【  ａ  ｅ  ｓ  ｔ  ｈ  ｅ  ｔ  ｉ  ｃ  】
@events.register(events.NewMessage(pattern=r"(?s)(.+ )?(?:\((.+)\))?\.vc(.+)?$", incoming=False))
async def vaporcase(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    before = event.pattern_match.group(1)
    message_text = event.pattern_match.group(2)
    after = event.pattern_match.group(3)

    if message_text:
        vaporwaved = re.sub(r"(.)", r"\1  ", "".join(vaporwave(message_text)))
        if not before:
            before = ""
        if not after:
            after = ""
        new_reply_str = f"{before} 【  {vaporwaved}】 {after}"
        await event.respond(new_reply_str, reply_to=reply_id)
    elif not reply_msg:
        pass
    else:
        new_reply_str = re.sub(r"(.)", r"\1  ", ''.join(vaporwave(reply_msg.raw_text)))
        await event.respond(f"【  {new_reply_str}】", reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")
