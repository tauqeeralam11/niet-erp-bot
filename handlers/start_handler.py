from utils.keyboards import home_menu
from config import OWNER_ID
async def start(update, context):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("❌ This bot is private.")
        return
    text = (
        "🎓 <b>NIET ERP Assistant</b>\n\n"
        "Quick access to official ERP academic notices.\n\n"
        "<b>Stay updated with:</b>\n"
        "• Exam schedules\n"
        "• Academic announcements\n"
        "• Important circulars\n\n"
        "Tap below to browse notices.\n\n"
        "<b>— Developed by Tauqeer Alam</b>"
    )
    await update.message.reply_text(
        text,
        reply_markup=home_menu(),
        parse_mode="HTML"
    )
    if "users" not in context.application.bot_data:
        context.application.bot_data["users"] = set()
    context.application.bot_data["users"].add(user_id)