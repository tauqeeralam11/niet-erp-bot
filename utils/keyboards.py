from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def home_menu():
    keyboard = [
        [InlineKeyboardButton("📢 Browse Latest Notices", callback_data="notices_0")]
    ]
    return InlineKeyboardMarkup(keyboard)