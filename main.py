import os
from telegram import Bot
from telegram.ext import ApplicationBuilder, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
GRUPO_ID = int(os.getenv("GRUPO_ID"))

async def enviar_mensagem(context: ContextTypes.DEFAULT_TYPE):
    mensagem = "🎯 Bilhete pronto: exemplo automático de palpite!"
    await context.bot.send_message(chat_id=GRUPO_ID, text=mensagem)

async def start_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(enviar_mensagem, 'interval', minutes=30, args=[app])
    scheduler.start()
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == '__main__':
    asyncio.run(start_bot())
