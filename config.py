import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ERP_USERNAME = os.getenv("ERP_USERNAME")
ERP_PASSWORD = os.getenv("ERP_PASSWORD")
BASE_URL = "https://niet.instituteoncloud.com"
OWNER_ID = int(os.getenv("OWNER_ID"))