import requests
import json
import re
import os
from bs4 import BeautifulSoup
from config import BASE_URL
session = requests.Session()
def login():
    login_url = f"{BASE_URL}/Account/Login"
    r = session.get(login_url)
    html = r.text
    token_match = re.search(
        r'name="__RequestVerificationToken" type="hidden" value="(.+?)"',
        html
    )
    if not token_match:
        return False
    token = token_match.group(1)
    payload = {
        "__RequestVerificationToken": token,
        "email": os.getenv("ERP_USERNAME"),
        "password": os.getenv("ERP_PASSWORD"),
        "rememberMe": "false"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": login_url
    }
    r = session.post(login_url, data=payload, headers=headers)
    return "Dashboard" in r.text
def get_notices():
    if not login():
        print("Login failed")
        return []
    url = f"{BASE_URL}/AcademicsUpload/GetNoticeList"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    r = session.get(url, headers=headers)
    if not r.text.strip():
        print("Empty ERP response")
        return []
    raw = json.loads(r.text)
    if isinstance(raw, str):
        data = json.loads(raw)
    else:
        data = raw
    notices = []
    for item in data["Table"][:200]:
        notices.append({
            "id": item["NoticeID"],
            "title": item["Title"]
        })
    print(f"Fetched {len(notices)} notices")
    return notices
def get_pdf_link(notice_id):
    url = f"{BASE_URL}/AcademicsUpload/DetailedViewOfNotice"
    payload = {
        "fc": f"View_{notice_id}"
    }
    r = session.post(url, data=payload)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all("a", href=True):
        if "amazonaws" in a["href"]:
            return a["href"].replace(" ", "%20")
    return None