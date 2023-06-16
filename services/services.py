from aiogram.filters import Text
from aiogram.types import Message
import random
from keyboards.keyboards import kb,kb2
from aiogram import Router



router: Router = Router()



def choice():
    return random.choice(['Ножницы', 'Бумага', 'Камень'])



@router.message(Text(['Бумага', 'Ножницы', 'Камень']))
async def game(message: Message):
    if message.text == choice():
        await message.answer(text=f"Оба пользователя выбрали {message.text}. Ничья!!\n"
        f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
    elif message.text == "Камень":
        if choice() == "Ножницы":
            await message.answer(text=f"Камень бьет ножницы! Вы победили!\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
        else:
            await message.answer(text=f"Бумага оборачивает камень! Вы проиграли.\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
    elif message.text == "Бумага":
        if choice() == "Камень":
            await message.answer(text=f"Бумага оборачивает камень! Вы победили!\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
        else:
            await message.answer(text=f"Ножницы режут бумагу! Вы проиграли.\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
    elif message.text == "Ножницы":
        if choice() == "Бумага":
            await message.answer(text="Ножницы режут бумагу! Вы победили!\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))
        else:
            await message.answer(text="Камень бьет ножницы! Вы проиграли.\n"
            f"Давай сыграем еще раз?",reply_markup= kb2.as_markup(resize_keyboard=True,one_time_keyboard = True))