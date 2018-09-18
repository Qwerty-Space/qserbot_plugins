from telethon import events, sync
from random import choice
import re


### STRING METHODS ###
# Capitalize message
async def capitalize(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    if not message_text:
        await event.respond(reply_msg.raw_text.capitalize(), reply_to=reply_id)
    else:
        await event.respond(message_text.capitalize(), reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

capitalize.event = events.NewMessage(pattern=r"(.+)?\.capitali[zs]e$", incoming=False)


# Make message lowercase
async def lower(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    if not message_text:
        await event.respond(reply_msg.raw_text.lower(), reply_to=reply_id)
    else:
        await event.respond(message_text.lower(), reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

lower.event = events.NewMessage(pattern=r"(.+)?\.lower$", incoming=False)


# Swap the case of a message
async def swapcase(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    if not message_text:
        await event.respond(reply_msg.raw_text.swapcase(), reply_to=reply_id)
    else:
        await event.respond(message_text.swapcase(), reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

swapcase.event = events.NewMessage(pattern=r"(.+)?\.swapcase$", incoming=False)


# Make message titlecase
async def title(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    if not message_text:
        await event.respond(reply_msg.raw_text.title(), reply_to=reply_id)
    else:
        await event.respond(message_text.title(), reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

title.event = events.NewMessage(pattern=r"(.+)?\.title$", incoming=False)


# Make message uppercase
async def upper(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    if not message_text:
        await event.respond(reply_msg.raw_text.upper(), reply_to=reply_id)
    else:
        await event.respond(message_text.upper(), reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

upper.event = events.NewMessage(pattern=r"(.+)?\.upper", incoming=False)


### OTHER STUFF ###
# Randomise the case of a message
async def randcase(event):
    sender = await event.get_sender()
    reply_msg = await event.get_reply_message()
    reply_id = event.reply_to_msg_id
    message_text = event.pattern_match.group(1)
    lst = [str.upper, str.lower]
    # reply_msg = ''.join(choice(lst)(c) for c in reply_msg)
    if not message_text:
        new_reply_str = ''.join(choice(lst)(c) for c in reply_msg.raw_text)
        await event.respond(new_reply_str, reply_to=reply_id)
    else:
        new_reply_str = ''.join(choice(lst)(c) for c in message_text)
        await event.respond(new_reply_str, reply_to=reply_id)
    await event.delete()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}")

randcase.event = events.NewMessage(pattern=r"(.+)?\.randcase$", incoming=False)


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

vaporcase.event = events.NewMessage(pattern=r"(.+ )?(?:\((.+)\))?.vc(.+)?", incoming=False)
