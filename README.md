# expenses_bot

A telegram bot recording your expenses.

## Features

- Logging expenses with "500 food" format
- Get your daily today's records with /today
- Get your this month's records with /month
- Get stats with /stats


## Tech Stack
Python, aiogram 3, python-dotenv, SQLite


## How to run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a bot via BotFather on Telegram and get your token.
4. Create a `.env` file and add your token: `BOT_TOKEN=your_token_here`
5. Run the bot: `python main.py`

## Project structure
- `main.py` — bot setup and handlers
- `storage.py` — Database, SQLite functions