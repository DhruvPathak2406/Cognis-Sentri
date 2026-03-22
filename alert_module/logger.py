from datetime import datetime
import os

LOG_FILE = "logs/alerts.log"

os.makedirs("logs", exist_ok=True)

def log_event(level, message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] [{level}] {message}\n")