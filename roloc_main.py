import logging
import asyncio

from aiohttp import web
from data.config import LOG_FILE

from handlers.start_handler import start_router
from handlers.user.help_handler import help_router
from handlers.user.about_handler import about_router
from handlers.user.app_from_handler import app_form_router

from handlers.admin.search_handler import search_router
from handlers.admin.change_handler import change_router
from handlers.admin.switch_user_menu import switch_router

from roloc_create import dp, roloc_bot, Bot, WEBHOOK_PATH, WEBHOOK_URL
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


# async def main():  # POLLING
#     dp.include_routers(
#         search_router,
#         change_router,
#         switch_router,
#         app_form_router,
#         start_router,
#         help_router,
#         about_router,
#     )
#     await dp.start_polling(roloc_bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE, filemode='w')
#     asyncio.run(main())

async def on_startup(bot: Bot) -> None: # WEBHOOK
    await bot.set_webhook(f"{WEBHOOK_URL}{WEBHOOK_PATH}")


def main() -> None:
    dp.include_routers(
        search_router,
        change_router,
        switch_router,
        app_form_router,
        start_router,
        help_router,
        about_router,
    )

    dp.startup.register(on_startup)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=roloc_bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=roloc_bot)
    web.run_app(app, host='127.0.0.1', port=5000)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename=LOG_FILE, filemode='w')
    main()
