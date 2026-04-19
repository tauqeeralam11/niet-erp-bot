import threading
import logging
from flask import Flask
from bot.bot import run_bot
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("ERP-BOT")
app = Flask(__name__)
@app.route("/")
def home():
    return "ERP Telegram Bot is running"
def run_web():
    """
    Run web server required by Render
    """
    logger.info("Starting web server for Render...")
    app.run(host="0.0.0.0", port=10000)
def main():
    logger.info("Starting ERP Telegram Bot...")
    web_thread = threading.Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()
    run_bot()
if __name__ == "__main__":
    main()