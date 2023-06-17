from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU
<<<<<<< HEAD
=======

>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909

router: Router = Router()

@router.message()
async def other(message: Message):
<<<<<<< HEAD
    await message.answer(text=LEXICON_RU['other_answer'])
=======
    await message.answer(text=LEXICON_RU['other_answer'],reply_markup=ReplyKeyboardRemove(),parse_mode='HTML')
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909
