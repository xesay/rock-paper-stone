from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU


router: Router = Router()

@router.message()
async def other(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'],reply_markup=ReplyKeyboardRemove(),parse_mode='HTML')