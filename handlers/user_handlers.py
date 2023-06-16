from aiogram.types import Message
from keyboards.keyboards import kb,kb2
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import LEXICON
from aiogram import Router


router: Router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=LEXICON['/start'],
    reply_markup=kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))

@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(text=f'<b><i>{LEXICON["/help"]}</i></b>',reply_markup=kb2.as_markup(resize_keyboard = True),parse_mode='HTML')

@router.message(Text('Давай'))
async def accept(message: Message):
    await message.answer(text=LEXICON['Давай'],reply_markup=kb.as_markup(resize_keyboard=True,one_time_keyboard=True))

@router.message(Text('Не хочу'))
async def no_accept(message: Message):
    await message.answer(text=LEXICON['Не хочу'])

