__all__ = []

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config.telegram_amo import config


class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(storage=MemoryStorage())
    
    async def _get_bot_dp(self):
        return self.bot, self.dp


telegram_bot_dp = TelegramBot(config.TELEGRAM_TOKEN)