import time
cache = {
    "notices": [],
    "timestamp": 0
}
CACHE_TIME = 600
def get_cache(fetch_function):
    current = time.time()
    if current - cache["timestamp"] > CACHE_TIME:
        cache["notices"] = fetch_function()
        cache["timestamp"] = current

    return cache["notices"]
def clear_cache():
    """
    Force refresh cache (used when new notices arrive)
    """
    cache["timestamp"] = 0