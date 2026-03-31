import time
from datetime import datetime

from .communicator import send_telegram
from .alarm import play_alarm
from .logger import log_event
from .arduino import trigger_hardware
class AlertSystem:

    def __init__(self):
        self.last_alert_time = 0
        self.cooldown = 8
        self.emergency_sent = False

    def execute(self, action, mode):
        if mode == "STOP":
         print("⚠ System stopped — no alert")
         return
        current_time = time.time()

        if current_time - self.last_alert_time < self.cooldown:
            print("⏳ Cooldown active")
            return

        self.last_alert_time = current_time

        timestamp = datetime.now().strftime("%H:%M:%S")

        message = f"""
🚨 ALERT LEVEL: {action}
🕒 Time: {timestamp}
"""

        print("\n" + "="*40)
        print(message)
        print("="*40 + "\n")

        if action == 0:
            self._safe()

        elif action == 1:
            self._notify(message, mode)

        elif action == 2:
            self._alarm(message, mode)

        elif action == 3:
            self._emergency(message, mode)

    # ----------------------------

    def _safe(self):
        print("✅ Safe")
        self.emergency_sent = False

    def _notify(self, message, mode):
        print("📩 Notification")

        if mode == "PROTECTOR":
            send_telegram(message)

        log_event("NOTIFY", message)

    def _alarm(self, message, mode):
        print("🔊 Alarm Triggered")
        play_alarm()

        if mode == "PROTECTOR":
            send_telegram("🚨 ALARM TRIGGERED")

        if mode == "DEFENDER":
            trigger_hardware()

        log_event("ALARM", message)

    def _emergency(self, message, mode):
        if self.emergency_sent:
            print("⚠️ Already sent")
            return

        print("🔥 EMERGENCY MODE")
        play_alarm()

        if mode == "PROTECTOR":
            send_telegram("🔥 CRITICAL ALERT!")
            send_telegram("📞 CALL ALERT! Intruder detected!")

        if mode == "DEFENDER":
            trigger_hardware()

        log_event("EMERGENCY", message)

        self.emergency_sent = True