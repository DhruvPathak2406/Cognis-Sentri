import requests

TOKEN = "8730480407:AAHPudHjQufY5ZbdzHC-YBQ8wAYuBl-y5xQ"
CHAT_ID = "6332722378"

def send_sms(message, to=None):  # keep name same for compatibility
    send_telegram(message)

def make_call(to=None):
    send_telegram("📞 CALL ALERT!\nIntruder detected!")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    print("Telegram response:", response.text)  # debug