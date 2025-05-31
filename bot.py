from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os

async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

TOKEN = os.getenv("BOT_TOKEN")  # Read from environment variable

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve_request))

print("Bot started...")
app.run_polling()