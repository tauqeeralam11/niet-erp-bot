import os
STATE_FILE = "last_notice.txt"
def load_last_notice_id():
    """
    Load last notice ID from file
    """
    if not os.path.exists(STATE_FILE):
        return None
    try:
        with open(STATE_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return None
def save_last_notice_id(notice_id):
    """
    Save latest notice ID
    """
    with open(STATE_FILE, "w") as f:
        f.write(str(notice_id))