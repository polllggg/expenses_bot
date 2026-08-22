import os
import asyncio
from os import getenv

from dotenv import load_dotenv

from storage import create_table, add_expense, get_expenses_by_date, get_expenses_by_month, get_stats
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello, how can I help you")




@dp.message(F.text, ~F.text.startswith("/"))
async def message_handler(message: Message) -> None:
    try:
        current_message = message.text.split()
        amount_spent = int(current_message[0])
        category = current_message[1]
        date_string = datetime.now().strftime("%Y-%m-%d")
        add_expense(amount_spent, category, date_string)
        await message.answer(f"got it: {amount_spent} for {category}")
    except ValueError:
        await message.answer("please send message that includes the amount spend and the category")
    except IndexError:
        await message.answer("please send message that also includes the category")

@dp.message(Command("today"))
async def cmd_today(message: Message):
    date_string = datetime.now().strftime("%Y-%m-%d")
    today_date = get_expenses_by_date(date_string)
    empty_string = ""
    for i in today_date:
        empty_string += f" {i[1]}  {i[2]}. \n"
    await message.answer(empty_string)


@dp.message(Command("month"))
async def cmd_month(message: Message):
    date_string = datetime.now().strftime("%Y-%m")
    date_string += "-%"
    this_month = get_expenses_by_month(date_string)
    empty_string = ""
    for i in this_month:
        empty_string += f" {i[1]}  {i[2]}. \n"
    await message.answer(empty_string)

@dp.message(Command("stats"))
async def cmd_stats(message: Message):
    current_stats = get_stats()
    empty_string = ""
    for i in current_stats:
        empty_string += f" {i[0]}  {i[1]}. \n"
    await message.answer(empty_string)


async def main():
    create_table()
    await dp.start_polling(bot)



asyncio.run(main())



