from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logger = logging.getLogger(__name__)


async def start_command(message: types.Message):
    try:
        telephone_btn = [[InlineKeyboardButton(text='📞 Поделиться контактом', callback_data='request_contact')]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=telephone_btn)

        await message.answer(
            'Добро пожаловать! Для продолжения поделитесь контактом:',
            reply_markup=keyboard,
        )
        logger.info("Команда /start обработана")
    except Exception as e:
        logger.error(f"Ошибка в start_command: {e}")
        raise


async def process_callback_telephone_btn(callback_query: types.CallbackQuery):
    try:
        logger.info(f"Получен callback: {callback_query.data}")
        
        # Правильный ответ на callback
        await callback_query.answer()  # Без параметров или с текстом
        
        # Отправка сообщения
        await callback_query.message.answer('Вы нажали кнопку "Поделиться контактом"!')
        logger.info("Callback обработан успешно")
    except Exception as e:
        logger.error(f"Ошибка обработки callback: {e}")
        await callback_query.answer("Произошла ошибка", show_alert=True)
        raise