from services.notice_service import fetch_notices
async def search(update, context):
    query = " ".join(context.args).lower()
    notices = fetch_notices()
    results = [n for n in notices if query in n["title"].lower()]
    if not results:
        await update.message.reply_text("No notices found.")
        return
    text = "🔎 Search Results\n\n"
    for notice in results[:10]:
        text += f"📄 {notice['title']}\n\n"
    await update.message.reply_text(text)