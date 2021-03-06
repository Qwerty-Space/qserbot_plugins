"""Converts celsius to fahrenheit and back.  Example:
"c 5°C in degrees f"
Accepts variations of "°C", for example "c", "degrees Celsius", or "degrees C".
Case insensitive.

patterns:
`(?i)^c (\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?c(elsius)? (to|in) (°|degrees)?f(ahrenheit)?$`

`(?i)^c (\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?f(ahrenheit)? (to|in) (°|degrees)?c(elsius)?$`
"""

import re
from telethon import events, sync
from .global_functions import probability


### FUNCTIONS ###
# Celsius to Fahrenheit
async def c_to_f(event, value):
    sum = round((value * 1.8) + 32, 2)
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    return sum

# Fahrenheit to Celsius
async def f_to_c(event, value):
    sum = round((value - 32) * 0.55555555555, 2)
    sender = await event.get_sender()
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    return sum


### INLINE ###
@events.register(events.NewMessage(pattern=re.compile(r"^c ?(\-?\d{1,9}(?:.\d\d?)?)( ?° ?| degrees)? ?c(elsius)? (to|in) (°|degrees)?f(ahrenheit)?$", re.I).search, incoming=False))
async def inline_c_to_f(event):
    c = float(event.pattern_match.group(1))
    result = await c_to_f(event, c)
    await event.delete()
    await event.respond(f"**{c} °C is:**  `{result} °F`", reply_to=event.reply_to_msg_id)


@events.register(events.NewMessage(pattern=re.compile(r"^c ?(\-?\d{1,9}(?:.\d\d?)?)( ?° ?| degrees)? ?f(ahrenheit)? (to|in) (°|degrees)?c(elsius)?$", re.I).search, incoming=False))
async def inline_f_to_c(event):
    f = float(event.pattern_match.group(1))
    result = await f_to_c(event, f)
    await event.delete()
    await event.respond(f"**{f} °F is:**  `{result} °C`", reply_to=event.reply_to_msg_id)


### MENTION ###
@events.register(events.NewMessage(pattern=re.compile(r"^(\w+).?(?: what is | what['’]s )?(\-?\d{1,9}(?:.\d\d?)?)( ?° ?| degrees)? ?c(elsius)? (to|in) (°|degrees)?f(ahrenheit)?\??$", re.I).search, incoming=True, chats=1001146038279, blacklist_chats=True))
async def mention_c_to_f(event):
    name = (await event.client.get_me()).first_name
    fname = re.sub(r"\W.+", "", name)
    username = (await event.client.get_me()).username
    c = float(event.pattern_match.group(2))
    result = await c_to_f(event, c)
    if re.match(fr"(?i)({fname}|{name}|{username})", event.pattern_match.group(1)):
        await event.reply(f"**{c} °C is:**  `{result} °F`")


@events.register(events.NewMessage(pattern=re.compile(r"^(\w+).?(?: what is | what['’]s )?(\-?\d{1,9}(?:.\d\d?)?)( ?° ?| degrees)? ?f(ahrenheit)? (to|in) (°|degrees)?c(elsius)?\??$", re.I).search, incoming=True, chats=1001146038279, blacklist_chats=True))
async def mention_f_to_c(event):
    name = (await event.client.get_me()).first_name
    fname = re.sub(r"\W.+", "", name)
    username = (await event.client.get_me()).username
    f = float(event.pattern_match.group(2))
    result = await f_to_c(event, f)
    if re.match(fr"(?i)({fname}|{name}|{username})", event.pattern_match.group(1)):
        await event.reply(f"**{f} °F is:**  `{result} °C`")
