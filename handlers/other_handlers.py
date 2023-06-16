from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router

router: Router = Router()

@router.message()
async def other(message: Message):
    await message.answer(text='Я вас не понимаю',reply_markup=ReplyKeyboardRemove())