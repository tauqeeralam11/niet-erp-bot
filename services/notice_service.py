from scrapers.notice_scraper import get_notices, get_pdf_link
from services.cache_service import get_cache, clear_cache
def fetch_notices(force_refresh=False):
    """
    Get notices from cache or ERP
    """
    if force_refresh:
        clear_cache()
    return get_cache(get_notices)
def fetch_pdf(notice_id):
    """
    Get PDF link for notice
    """
    return get_pdf_link(notice_id)