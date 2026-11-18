# Expenses Bot — Telegram expense tracker

A Telegram bot that turns free-form messages like `500 groceries` into structured,
queryable spending records. Built to practice async Python and a clean data layer
end to end.

## What it does

- **Natural-language logging:** send `500 groceries` and it parses the amount and
  category and stores them — no forms, no fixed syntax to memorise.
- **Reports on demand:**
  - `/today` — today's records
  - `/month` — this month's records
  - `/stats` — totals by category
- Persists everything to a local SQLite database.

## How it's built

- **Async, event-driven:** `aiogram 3` with `asyncio` — handlers are non-blocking,
  so the bot stays responsive under concurrent messages.
- **Data layer:** a normalised SQLite schema with aggregation queries that produce
  the daily, monthly and per-category views.
- **Config:** bot token via a `.env` file (`python-dotenv`) — no secrets in code.
- **Structure:**
  - `main.py` — bot setup and command handlers
  - `storage.py` — database access and aggregation queries

## Run locally

```bash
pip install -r requirements.txt
# create a bot via @BotFather, then:
echo "BOT_TOKEN=your_token_here" > .env
python main.py
```

## What this project is about

Shipping a small but complete product: parsing messy human input into structured
data, modelling it in a relational schema, and exposing it through an async
interface — rather than a script that only runs on my machine.

## Tech stack

Python · aiogram 3 · asyncio · SQLite · python-dotenv
