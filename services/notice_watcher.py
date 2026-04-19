import logging
from services.notice_service import fetch_notices, fetch_pdf
from services.cache_service import clear_cache
from utils.notice_state import load_last_notice_id, save_last_notice_id
logger = logging.getLogger(__name__)
last_notice_id = load_last_notice_id()
async def check_new_notices(context):
    global last_notice_id
    try:
        notices = fetch_notices(force_refresh=True)
        if not notices:
            return
        users = context.application.bot_data.get("users", [])
        if last_notice_id is None:
            last_notice_id = notices[0]["id"]
            save_last_notice_id(last_notice_id)
            logger.info("Initialized last_notice_id: %s", last_notice_id)
            return
        new_notices = []
        for notice in notices:
            if notice["id"] == last_notice_id:
                break
            new_notices.append(notice)
        if not new_notices:
            return
        last_notice_id = notices[0]["id"]
        save_last_notice_id(last_notice_id)
        clear_cache()
        new_notices.reverse()
        for notice in new_notices:
            logger.info("New notice detected: %s", notice["title"])
            pdf_url = fetch_pdf(notice["id"])
            for user in users:
                if pdf_url:
                    await context.bot.send_document(
                        chat_id=user,
                        document=pdf_url,
                        caption=f"📢 New ERP Notice\n\n{notice['title']}"
                    )
                else:
                    await context.bot.send_message(
                        chat_id=user,
                        text=f"📢 New ERP Notice\n\n{notice['title']}"
                    )
    except Exception as e:
        logger.error("Error in notice watcher: %s", e)