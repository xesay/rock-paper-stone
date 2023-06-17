import random
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU
<<<<<<< HEAD

=======
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909

router: Router = Router()




<<<<<<< HEAD
# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя 
=======
def choice():
    return random.choice(['rock', 'paper', 'scissors'])


>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception


<<<<<<< HEAD
# Функция, определяющая победителя
=======
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
<<<<<<< HEAD
        return 'bot_won'
=======
        return 'bot_won'
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909
