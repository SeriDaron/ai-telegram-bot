import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from config import settings
from database import init_db, add_user

# Configure logging to monitor bot activity in the terminal
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Initialize the bot and dispatcher
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Build a convenient button menu for the customer
def get_main_keyboard():
    kb = [
        [KeyboardButton(text="📊 View Analytics"), KeyboardButton(text="🤖 Ask AI Assistant")],
        [KeyboardButton(text="💼 About Nexus.AI"), KeyboardButton(text="📞 Contact Support")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """/start command handler"""
    # Save the user to the local database
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "unknown",
        full_name=message.from_user.full_name
    )
    
    welcome_text = (
        f"Hello, {html.bold(message.from_user.full_name)}! 👋\n\n"
        f"Welcome to {html.bold('Nexus.AI Business Bot')}.\n"
        f"I am a demo AI assistant (simulated replies).\n\n"
        f"Use the menu below to explore analytics or interact with the AI co-pilot."
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """/help command handler"""
    help_text = (
        f"🤖 {html.bold('Available Commands & Features:')}\n\n"
        f"/start - Restart the bot and update registration\n"
        f"/help - Show this guide\n\n"
        f"👉 Use mobile keyboard buttons to check metrics and talk to AI."
    )
    await message.answer(help_text)

@dp.message(F.text == "📊 View Analytics")
async def handle_analytics(message: Message):
    """Business metrics report triggered by the menu button"""
    analytics_text = (
        f"📈 {html.bold('Nexus.AI Real-Time Metrics:')}\n\n"
        f"• Total Revenue: $48,259.80 (+12.5%)\n"
        f"• Active Customers: 1,248 (+8.2%)\n"
        f"• Conversion Rate: 3.42% (-0.4%)\n"
        f"• AI Automations Run: 14,892 (+24.1%)"
    )
    await message.answer(analytics_text)

@dp.message(F.text == "💼 About Nexus.AI")
async def handle_about(message: Message):
    """Company information"""
    about_text = (
        f"🚀 {html.bold('About Our Automation Ecosystem')}\n\n"
        f"Nexus.AI bridges the gap between raw corporate data and intelligent decisions. "
        f"This bot demonstrates server-side background operations, localized architecture, "
        f"and production-grade asynchronous logic built for high-scale production portfolios."
    )
    await message.answer(about_text)

@dp.message(F.text == "📞 Contact Support")
async def handle_support(message: Message):
    """Support contacts"""
    # Fixed f-string so the email renders correctly
    support_text = f"📬 For enterprise inquiries, contact our core team at: support@nexus-ai.dev"
    await message.answer(support_text)

@dp.message()
async def ai_message_handler(message: Message) -> None:
    """Handle free-text queries (simulated LLM API integration)"""
    user_text = message.text.lower()
    
    # Guard against double-triggering when the user presses other menu buttons
    if message.text in ["📊 View Analytics", "💼 About Nexus.AI", "📞 Contact Support"]:
        return

    # Simulate background AI processing
    waiting_msg = await message.answer("⏳ <i>Processing your query...</i>")
    await asyncio.sleep(1.2) # Short delay for realism
    
    # Basic agent response logic
    reply = "I've analyzed your text. To get custom insights, please use the predefined operational dashboard buttons."
    
    # Use any() for flexible keyword matching
    if any(word in user_text for word in ["customer", "client"]):
        reply = "Data Analysis: You currently have 1,248 active profiles. System logs show peak conversion periods between 2 PM and 5 PM."
    elif any(word in user_text for word in ["revenue", "sales"]):
        reply = "Financial Report: Revenue is stable at $48,259.80. The 12.5% monthly spike correlates with the launch of automated AI-flows."
    
    # Remove the waiting message and send the final reply
    await waiting_msg.delete()
    await message.answer(reply)

async def main() -> None:
    # Initialize the SQLite database
    await init_db()
    # Start polling the Telegram servers
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
