import time
from .notifier import show_notification
from .alarm import play_alarm
from .communicator import send_sms, make_call
from .logger import log_event
import config

class AlertSystem:
    def __init__(self):
        self.last_alert_time = 0
        self.emergency_sent = False
        self.start_time = None

    def execute(self, action):
        current_time = time.time()

        # Cooldown protection
        if current_time - self.last_alert_time < config.COOLDOWN:
            return

        self.last_alert_time = current_time

        # Track escalation time
        if self.start_time is None:
            self.start_time = current_time

        duration = current_time - self.start_time

        # Smart escalation upgrade
        if duration > config.ESCALATION_TIME:
            action = max(action, 3)

        # Execute actions
        if action == 0:
            return

        elif action == 1:
            self._handle_notification()

        elif action == 2:
            self._handle_alarm()

        elif action == 3:
            self._handle_emergency()

    # ---------- HANDLERS ----------

    def _handle_notification(self):
        message = "⚠️ Suspicious activity detected"
        show_notification(message)
        log_event("NOTIFICATION", message)

    def _handle_alarm(self):
        message = "🚨 Threat detected"
        show_notification(message)
        play_alarm()
        log_event("ALARM", message)

    def _handle_emergency(self):
        message = "🔥 CRITICAL ALERT: Intruder detected!"
        show_notification(message)
        play_alarm()

        if not self.emergency_sent:
            if config.ENABLE_SMS:
                send_sms(message, config.OWNER_NUMBER)
                send_sms(message, config.EMERGENCY_NUMBER)

            if config.ENABLE_CALL:
                make_call(config.OWNER_NUMBER)
                make_call(config.EMERGENCY_NUMBER)

            log_event("EMERGENCY", message)
            self.emergency_sent = True