import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()
TOKEN = "{{sensitive_data}}"
bot = Bot(token=TOKEN)

test = {"tg_id": "{{sensitive_data}}",
        "amount": "320"}


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n"
                         f" I am the bot who notifies you about incoming")


async def notify(tg_id: int, amount: int):
    try:
        if tg_id and amount:
            await bot.send_message(tg_id, f"You received {amount} on your balance!")
        else:
            print("You didn't provide enough information")
    except Exception as e:
        print(f"ERROR:\n{e}")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
