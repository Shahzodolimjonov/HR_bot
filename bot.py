import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from start import router as start_router
from handlers.vakansiya import router as vakansiya_router
from handlers.resume import router as resume_router

from config import BOT_TOKEN, create_tables

dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    description = (
        "📢 Developer Jobs – Rasmiy Reklama Menejeri!\n\n"

        "👋 Men Developer Jobs kanali reklama menejeriman!\n\n"
        "📌 Bot orqali faqat reklama mavzusida xabar yuboring.\n\n"
        "⚠️ Boshqa mavzulardagi xabarlar ko‘rib chiqilmaydi.\n\n"

    )
    await bot.set_my_description(description)

    await bot.set_my_commands([BotCommand(command="start", description="Botni ishga tushirish")])
    dp.include_routers(start_router,
                       vakansiya_router,
                       resume_router,
                       )
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
