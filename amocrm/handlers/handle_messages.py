import aiogram.types as types
from keyboards.start_keyboard import start_keyboard


async def start_command(message: types.Message):
    keyboard = start_keyboard()
    await message.answer('Чтобы продолжить работу дальше, поделитесь контактом')


async def process_contact_request(callback: types.CallbackQuery):
    contact_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_keyboard.add(types.KeyboardButton('☎️ Отправить свой контакт', request_contact=True))
    await callback.message.answer('Нажмите кнопку ниже, чтобы отправить ваш контакт:', reply_markup=contact_keyboard)
    await callback.answer()
