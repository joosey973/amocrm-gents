from utils.initializations import create_bot
from config.telegram_amo import config
import handlers.handle_messages as commands

from contextlib import asynccontextmanager

from fastapi import FastAPI
from aiogram.filters import Command


@asynccontextmanager
async def lifespan(app: FastAPI):
    bot, dp = await create_bot(config.TELEGRAM_TOKEN)

    dp.message.register(commands.start_command, Command('start'))
    dp.callback_query.register(commands.process_contact_request, F.data == 'request_contact')

    yield


app = FastAPI(lifespan=lifespan)
