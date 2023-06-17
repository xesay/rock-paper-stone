from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
bt_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
bt_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
bt_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
kb.row(bt_1,bt_2,bt_3)

kb2: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
bt_4: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
bt_5: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])
kb2.row(bt_4,bt_5)
