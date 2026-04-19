from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from bot.routes import register_routes
from services.notice_watcher import check_new_notices
def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_routes(app)
    app.job_queue.run_repeating(
        check_new_notices,
        interval=300,
        first=10
    )
    print("🤖 Bot started")
    app.run_polling()