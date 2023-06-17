from aiogram import Bot, Dispatcher
from config_data.config import load_config,Config
from handlers import user_handlers, other_handlers
import asyncio
<<<<<<< HEAD
from keyboards.set_menu import set_main_menu
=======
from services import services
import logging

logger = logging.getLogger(__name__)
>>>>>>> 62fb27a7bab5a1249665a58143c42832353e4909


async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    api: Config = load_config('env.txt')
    bot: Bot = Bot(api.tg_bot.token)
    dp: Dispatcher = Dispatcher()


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
