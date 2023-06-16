from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
bt_1: KeyboardButton = KeyboardButton(text='Камень')
bt_2: KeyboardButton = KeyboardButton(text='Ножницы')
bt_3: KeyboardButton = KeyboardButton(text='Бумага')
kb.row(bt_1,bt_2,bt_3)

kb2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
bt_4: KeyboardButton = KeyboardButton(text='Давай')
bt_5: KeyboardButton = KeyboardButton(text='Не хочу')
kb2.row(bt_4,bt_5)
