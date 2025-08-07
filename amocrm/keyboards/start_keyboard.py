from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text='Отправить контакт',
        callback_data='request_contact'
    )
    keyboard.add(button)
    return keyboard
