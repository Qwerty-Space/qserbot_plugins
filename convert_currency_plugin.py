r"""Converts two different currencies using the [European Central Bank's exchange rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).

Example: "c GBP to/in USD" (case insensitive).
You can also specify an amount of said currency:
"c 5 GBP to USD".

pattern:  `(?i)^c ?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})$`
"""

import asyncio
from telethon import events
from .global_functions import log
from currency_converter import CurrencyConverter
c = CurrencyConverter()


# Convert Currency
@events.register(events.NewMessage(pattern=r"(?i)^c ?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})$", outgoing=True))
async def currency(event):
    fromval = event.pattern_match.group(1)
    if not fromval:
        fromval = 1
    fromcur = event.pattern_match.group(2).upper()
    tocur = event.pattern_match.group(3).upper()
    try:
        result = round(c.convert(fromval, fromcur, tocur), 2)
        await log(event, result)
        await event.delete()
        await event.respond(f"**{fromval} {fromcur} is:**  `{result} {tocur}`", reply_to=event.reply_to_msg_id)
    except ValueError:
        await log(event, "NOT AVAILABLE")
        await event.delete()
        link = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
        message = await event.respond(
            f"**Sorry, that currency is not supported yet.**\nFor a list of supported currencies [click here.]({link})",
            link_preview=False
        )
        await asyncio.sleep(3)
        await message.delete()
