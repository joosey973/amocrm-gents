import asyncio

from aiogram.filters import Command
from config.telegram_amo import config
from utils.initializations import create_bot
import handlers.handle_messages as commands

from aiogram import F


async def main():
    bot, dp = await create_bot(config.TELEGRAM_TOKEN)

    await bot.delete_webhook(drop_pending_updates=True)

    dp.message.register(commands.start_command, Command('start'))
    dp.callback_query.register(commands.process_contact_request, F.data == 'request_contact')

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
