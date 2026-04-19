from telegram.ext import CommandHandler, CallbackQueryHandler
from handlers.start_handler import start
from handlers.notice_handler import button
def register_routes(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))