import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("8576500709:AAGZzZk95NdORL61N_crHOFbcUV27DC2QFk")

async def start(update: Update, context):
    await update.message.reply_text("សួស្តី 👋 បញ្ជូន Link YouTube ឬ TikTok មកខ្ញុំ 😄")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"អ្នកផ្ញើ link: {text}\n(ជំហានបន្ទាប់ យើងនឹងបន្ថែម feature download)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
