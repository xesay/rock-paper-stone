from aiogram import Bot, Dispatcher
from config_data.config import load_config,Config
from handlers import user_handlers, other_handlers
import asyncio
from keyboards.set_menu import set_main_menu


async def main():

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
