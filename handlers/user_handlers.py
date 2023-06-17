from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.keyboards import kb,kb2
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import LEXICON_RU
from aiogram import Router
from services.services import choice, get_winner

router: Router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
    reply_markup=kb2.as_markup(resize_keyboard=True,one_time_keyboard = True),parse_mode='HTML')

@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.answer(text=f'<b><i>{LEXICON_RU["/help"]}</i></b>',reply_markup=kb2.as_markup(resize_keyboard = True),parse_mode='HTML')

@router.message(Text(LEXICON_RU['yes_button']))
async def accept(message: Message):
    await message.answer(text=LEXICON_RU['yes'],reply_markup=kb.as_markup(resize_keyboard=True,one_time_keyboard=True),parse_mode='HTML')

@router.message(Text(LEXICON_RU['no_button']))
async def no_accept(message: Message):
    await message.answer(text=LEXICON_RU['no'],parse_mode='HTML')

@router.message(Command(commands=['stat']))
async def cmd_stat(message: Message):
    await message.answer(text=f'Вы сыграли раз и выиграли раз')


@router.message(Text([LEXICON_RU['rock'],LEXICON_RU['paper'],LEXICON_RU['scissors']]))
async def game(message: Message):
    computer = choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}'
    f'- {LEXICON_RU[computer]}')
    winner = get_winner(message.text, computer)
    await message.answer(text=LEXICON_RU[winner],parse_mode='HTML',reply_markup=kb2.as_markup(resize_keyboard = True))