from aiogram.utils.keyboard import ReplyKeyboardBuilder
<<<<<<< HEAD
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb = yes_no_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)
=======
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
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909
