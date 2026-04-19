# 🎓 NIET ERP Telegram Bot

A powerful Telegram bot that fetches and delivers **latest academic notices from NIET ERP** directly to your chat — with PDF access and real-time notifications.

---

## 🚀 Features

- :loudspeaker: Browse latest ERP notices  
- :page_facing_up: Download notice PDFs directly in Telegram  
- :mag: Search notices by keyword  
- :arrow_right: Pagination (Next / Previous navigation)  
- :bell: Automatic notification when new notice arrives  
- :zap: Fast performance with caching  
- :lock: Private access (Owner-based control)

---

## 🛠 Tech Stack

* Python
* python-telegram-bot
* Requests
* BeautifulSoup (Web Scraping)
* APScheduler (Background jobs)
* Flask (for deployment)
* Render (hosting)

---

## 📂 Project Structure

```
BOT-MAIN/
│
├── bot/
│   ├── bot.py
│   ├── handlers.py
│   ├── routes.py
│
├── handlers/
│   ├── notice_handler.py
│   ├── search_handler.py
│   ├── start_handler.py
│
├── scrapers/
│   ├── notice_scraper.py
│
├── services/
│   ├── cache_service.py
│   ├── notice_service.py
│   ├── notice_watcher.py
│
├── utils/
│   ├── keyboards.py
│   ├── notice_state.py
│
├── config.py
├── main.py
├── requirements.txt
└── .env   (not included in repo)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/tauqeeralam11/niet-erp-bot.git
cd niet-erp-bot
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` File

Create a `.env` file in root directory:

```
BOT_TOKEN=your_telegram_bot_token
ERP_USERNAME=your_erp_email
ERP_PASSWORD=your_erp_password
OWNER_ID=your_telegram_user_id
```

---

### 4️⃣ Run the Bot

```bash
python main.py
```

---

## 🤖 Bot Commands

| Command        | Description          |
| -------------- | -------------------- |
| `/start`       | Start bot            |
| Browse Button  | View notices         |
| Inline Buttons | Open PDFs / Navigate |

---

## 🔔 Notification System

* Runs every **5 minutes**
* Detects new notices automatically
* Sends alert + PDF directly to user

---

## ⚡ How It Works

1. Logs into NIET ERP
2. Fetches notices using internal API
3. Caches data for performance
4. Displays notices in Telegram UI
5. Extracts PDF links from notice page
6. Sends notifications when new notice appears

---

## 🔐 Security Notes

* Credentials are stored in `.env`
* `.env` is NOT uploaded to GitHub
* Do not share your ERP credentials publicly

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.

* Not officially affiliated with NIET
* Do not misuse ERP systems
* Follow institutional policies

---

## 👨‍💻 Author

**Tauqeer Alam**

---

## ⭐ Future Improvements

* Public multi-user support
* UI enhancements
* Database integration
* Faster async scraping

---

## ❤️ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share with friends

---

## 🚀 Status

✅ Fully Working
✅ Pagination Fixed
✅ Notification System Active
