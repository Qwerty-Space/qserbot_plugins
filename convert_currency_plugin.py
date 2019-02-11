r"""Converts two different currencies using the [European Central Bank's exchange rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).

Example: "c GBP to/in USD" (case insensitive).
You can also specify an amount of said currency:
`c 5 GBP to USD`.

Also works inline by asking the user what currency is in currency.  Example:
Alice: `Bob, what's 5 GBP in USD?`
Punctuation optional.

patterns:
`(?i)^c ?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})$`

`(?i)^(\w+).?(?: what is | what['’]s )?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})\??$`
"""

import re
import asyncio
from telethon import events
from .global_functions import log
from currency_converter import CurrencyConverter
c = CurrencyConverter()

# Convert currency
async def convert(event, fromval, fromcur, tocur, reply):
    try:
        result = round(c.convert(fromval, fromcur, tocur), 2)
        await log(event, result)
        await event.respond(f"**{fromval} {fromcur} is:**  `{result} {tocur}`", reply_to=reply)
    except ValueError:
        await log(event, "NOT AVAILABLE")
        link = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
        message = await event.respond(
            f"**Sorry, that currency is not supported yet.**\nFor a list of supported currencies [click here.]({link})",
            link_preview=False
        )
        await asyncio.sleep(3)
        await message.delete()


# Inline
@events.register(events.NewMessage(
    pattern=r"(?i)^c ?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})$",
    outgoing=True
    )
)
async def inline(event):
    fromval = event.pattern_match.group(1)
    if not fromval:
        fromval = 1
    fromcur = event.pattern_match.group(2).upper()
    tocur = event.pattern_match.group(3).upper()
    await convert(event, fromval, fromcur, tocur, event.reply_to_msg_id)
    await event.delete()

# By mention
@events.register(events.NewMessage(
    pattern=r"(?i)^(\w+).?(?: what is | what['’]s )?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})\??$",
    incoming=True,
    chats=1001146038279,
    blacklist_chats=True
    )
)
async def mention(event):
    fromval = event.pattern_match.group(2)
    if not fromval:
        fromval = 1
    fromcur = event.pattern_match.group(3).upper()
    tocur = event.pattern_match.group(4).upper()
    name = (await event.client.get_me()).first_name
    fname = re.sub(r"\W.+", "", name)
    username = (await event.client.get_me()).username

    if re.match(fr"(?i)({fname}|{name}|{username})", event.pattern_match.group(1)):
        await convert(event, fromval, fromcur, tocur, event)
