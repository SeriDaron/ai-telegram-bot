# Nexus.AI Telegram Business Assistant

An asynchronous Telegram bot built with **Python** and **aiogram 3**, with SQLite persistence and a simulated AI assistant. It demonstrates a clean, production-style bot structure.

> **Demo note:** the AI replies are simulated with keyword logic and a short delay. The handler is a drop-in spot for a real LLM API (e.g. Claude or OpenAI).

## Features

- **Async core:** non-blocking handlers built on aiogram 3.
- **Reply keyboard menu:** analytics, company info, and support buttons.
- **User and chat logging:** `aiosqlite` stores registered users and conversations.
- **Typed configuration:** `pydantic-settings` loads secrets from environment variables / `.env`.
- **Simulated AI assistant:** free-text questions get context-aware answers (customers, revenue, ...).

## Tech Stack

Python 3.9+ · aiogram 3.15 · pydantic-settings · aiosqlite

## Project Structure

```text
.
├── bot.py            # Handlers, keyboard menu, polling entry point
├── config.py         # Typed settings (BOT_TOKEN, AI_API_KEY)
├── database.py       # Async SQLite setup and queries
└── requirements.txt
```

## Getting Started

```bash
git clone https://github.com/SeriDaron/ai-telegram-bot.git
cd ai-telegram-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file (get a token from [@BotFather](https://t.me/BotFather)):

```env
BOT_TOKEN=your_telegram_bot_token
```

Run the bot:

```bash
python3 bot.py
```

## Security

Secrets are never committed: `.env` and the local database are git-ignored.

## Need something similar?

I build Telegram bots, AI assistants, and business automation. Feel free to reach out.
