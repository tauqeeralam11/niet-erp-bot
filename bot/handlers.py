import re
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from scrapers import notice_scraper
notices_cache = []
async def show_notices(update, context, page=0):
    global notices_cache
    if not notices_cache:
        notices_cache = notice_scraper.get_notices()
    start = page * 3
    end = start + 3
    selected = notices_cache[start:end]
    text = "📢 Latest Notices\n\n"
    keyboard = []
    for i, notice in enumerate(selected):
        text += f"{i+1}. {notice['title']}\n"
        keyboard.append([
            InlineKeyboardButton(
                f"📄 PDF {i+1}",
                callback_data=f"pdf_{start+i}"
            )
        ])
    keyboard.append([
        InlineKeyboardButton(
            "Next ➡",
            callback_data=f"notices_{page+1}"
        )
    ])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        text,
        reply_markup=reply_markup
    )
async def send_pdf(update, context, index):
    notice = notices_cache[index]
    pdf_url = notice_scraper.get_pdf_link(notice["id"])
    if not pdf_url:
        await update.callback_query.message.reply_text("PDF not found.")
        return
    await update.callback_query.message.reply_document(pdf_url)