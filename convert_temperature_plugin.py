import re
from telethon import events, sync
from global_functions import probability

### INLINE ###
async def c_to_f(event):
    sender = await event.get_sender()
    c = int(event.pattern_match.group(1))
    sum = (c * 1.8) + 32
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    await event.edit(f"**{c} °C is:**  `{sum} °F`")

c_to_f.event = events.NewMessage(pattern=re.compile(r"^c(\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?c(elsius)? (to|in) (°|degrees)?f(ahrenheit)?$", re.I).search, incoming=False)


async def f_to_c(event):
    sender = await event.get_sender()
    f = int(event.pattern_match.group(1))
    sum = (f - 32) * 0.55555555555
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    await event.edit(f"**{f} °F is:**  `{sum} °C`")

f_to_c.event = events.NewMessage(pattern=re.compile(r"^c(\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?f(ahrenheit)? (to|in) (°|degrees)?c(elsius)?$", re.I).search, incoming=False)


### MENTION ###
async def reply_c_to_f(event):
    sender = await event.get_sender()
    c = int(event.pattern_match.group(1))
    sum = (c * 1.8) + 32
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    await event.reply(f"**{c} °C is:**  `{sum} °F`")

reply_c_to_f.event = events.NewMessage(pattern=re.compile(r"^(?:@BobTheBanana|Bob).?(?: what is | what's )?(\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?c(elsius)? (to|in) (°|degrees)?f(ahrenheit)?\??$", re.I).search, incoming=True, chats=1001146038279, blacklist_chats=True)


async def reply_f_to_c(event):
    sender = await event.get_sender()
    f = int(event.pattern_match.group(1))
    sum = (f - 32) * 0.55555555555
    print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {sum}")
    await event.reply(f"**{f} °F is:**  `{sum} °C`")

reply_f_to_c.event = events.NewMessage(pattern=re.compile(r"^(?:@BobTheBanana|Bob).?(?: what is | what's )?(\d{1,9}|-\d{1,9})( ?° ?| degrees)? ?f(ahrenheit)? (to|in) (°|degrees)?c(elsius)?\??$", re.I).search, incoming=True, chats=1001146038279, blacklist_chats=True)
