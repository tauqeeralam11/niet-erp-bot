from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from services.notice_service import fetch_notices, fetch_pdf
from config import OWNER_ID
notices_cache = []
def build_ui(page):
    per_page = 4
    start = page * per_page
    end = start + per_page
    selected = notices_cache[start:end]
    text = (
        "📢 Latest Academic Notices\n"
        "━━━━━━━━━━━━━━━━━━\n"
    )
    keyboard = []
    for i, notice in enumerate(selected):
        serial = start + i + 1
        title = notice["title"]
        text += f"{serial}. {title}\n"
        short_title = title[:35] + "..." if len(title) > 35 else title
        keyboard.append([
            InlineKeyboardButton(
                f"📄 {short_title}",
                callback_data=f"pdf_{start+i}"
            )
        ])
    text += "━━━━━━━━━━━━━━━━━━"
    nav = []
    if start > 0:
        nav.append(
            InlineKeyboardButton("⬅ Prev", callback_data=f"notices_{page-1}")
        )
    if end < len(notices_cache):
        nav.append(
            InlineKeyboardButton("Next ➡", callback_data=f"notices_{page+1}")
        )
    if nav:
        keyboard.append(nav)
    return text, InlineKeyboardMarkup(keyboard)
async def show_notices(update, context, page, new_message=False):
    query = update.callback_query
    global notices_cache
    if not notices_cache:
        notices_cache = fetch_notices()
        print("Notices loaded:", len(notices_cache))
    text, markup = build_ui(page)
    if new_message:
        await query.message.reply_text(
            text,
            reply_markup=markup
        )
    else:
        await query.message.edit_text(
            text,
            reply_markup=markup
        )
async def send_pdf(update, context, index):
    query = update.callback_query
    notice = notices_cache[index]
    title = notice["title"]
    pdf_url = fetch_pdf(notice["id"])
    if not pdf_url:
        await query.answer("PDF not available", show_alert=True)
        return
    await query.message.reply_document(
        document=pdf_url,
        caption=f"📄 {title}"
    )
async def button(update, context):
    query = update.callback_query
    if query.from_user.id != OWNER_ID:
        await query.answer("❌ Private bot", show_alert=True)
        return
    await query.answer()
    data = query.data
    if data.startswith("notices"):
        page = int(data.split("_")[1])
        if page == 0 and query.message.text.startswith("🎓 NIET ERP Assistant"):
            await show_notices(update, context, page, new_message=True)
        else:
            await show_notices(update, context, page)
    elif data.startswith("pdf"):
        index = int(data.split("_")[1])
        await send_pdf(update, context, index)