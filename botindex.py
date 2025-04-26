from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Твой Telegram user ID
ADMIN_ID = 7436941173

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Проверяем, есть ли сообщение
    if update.message:
        await context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

# Инициализация бота
app = ApplicationBuilder().token("7548199893:AAHJHg96mu3N_GxsSMabjvrsKqPrD5P-hEA").build()

# Обработка всех входящих сообщений
app.add_handler(MessageHandler(filters.ALL, forward_message))

# Запуск
app.run_polling()
