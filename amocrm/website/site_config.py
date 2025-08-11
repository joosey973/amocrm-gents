from utils.initializations import telegram_bot_dp
from config.telegram_amo import config
import handlers.handle_messages as commands

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from aiogram.filters import Command
from aiogram import F
from aiogram.types import Update

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация бота и диспетчера
    bot, dp = await telegram_bot_dp._get_bot_dp()

    # Регистрация обработчиков
    dp.message.register(commands.start_command, Command('start'))
    dp.callback_query.register(commands.process_callback_telephone_btn, F.data == 'request_contact')

    # Установка вебхука
    await bot.set_webhook(
        url='https://6e9fe908bb2f.ngrok-free.app/tg-webhook',
        # drop_pending_updates=True
    )

    # Сохраняем бота и диспетчер в состоянии приложения
    app.state.bot = bot
    app.state.dp = dp

    yield

    # await bot.session.close()


@app.post("/tg-webhook")
async def webhook_handler(request: Request):
    bot = request.app.state.bot
    dp = request.app.state.dp
    
    update_data = await request.json()
    print(update_data)
    update = Update.model_validate(update_data)
    await dp.feed_update(bot, update)
    
    return {"status": "ok"}

app.router.lifespan_context = lifespan