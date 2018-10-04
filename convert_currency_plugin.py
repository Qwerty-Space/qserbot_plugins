from time import sleep
from telethon import events
from currency_converter import CurrencyConverter
c = CurrencyConverter()


# Convert Currency
async def currency(event):
    sender = await event.get_sender()  # Get the sender

    fromval = event.pattern_match.group(1)
    if not fromval:
        fromval = 1
    fromcur = event.pattern_match.group(2).upper()
    tocur = event.pattern_match.group(3).upper()
    try:
        result = round(c.convert(fromval, fromcur, tocur), 2)
        print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}: {event.pattern_match.string}: {result}")
        await event.delete()
        await event.respond(f"**{fromval} {fromcur} is:**  `{result} {tocur}`", reply_to=event.reply_to_msg_id)
    except ValueError:
        print(f"[{event.date.strftime('%c')}] [{sender.id}] {sender.username}:  {event.pattern_match.string}:  NOT AVAILABLE")
        await event.delete()
        link = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
        message = await event.respond(
            f"**Sorry, that currency is not supported yet.**\nFor a list of supported currencies [click here.]({link})",
            link_preview=False
        )
        sleep(3)
        await message.delete()


currency.event = events.NewMessage(pattern=r"^c ?(\d{1,9}|\d{1,9}\.\d\d?)? ?(\D{3}) (?:to|in) (\D{3})$", outgoing=True)
