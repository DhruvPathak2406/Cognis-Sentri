import tkinter as tk
from tkinter import scrolledtext
from alert_module.alert import AlertSystem
from recognition_module.Afacerecog import recognize_person
from registration_module.register import register_face
import tkinter.simpledialog as simpledialog
import threading

# ✅ RL IMPORTS (ADDED)
from DecisionEngine.state import get_state
from DecisionEngine.agent import decide_action, ACTIONS
from DecisionEngine.learning import train
from datetime import datetime


class Dashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Cognis-Sentri AI Security System")
        self.root.geometry("1000x650")
        self.root.configure(bg="#121212")
        self.alert = AlertSystem()
        self.mode = tk.StringVar(value="STOP")

        # ✅ RL INIT (ADDED)
        train(5000)
        self.attempts = 0

        # ================= TITLE =================
        tk.Label(root, text="Cognis-Sentri Security Dashboard",
                 font=("Arial", 18, "bold"),
                 fg="white", bg="#121212").pack(pady=10)

        # ================= MAIN FRAME =================
        main = tk.Frame(root, bg="#121212")
        main.pack(fill="both", expand=True)

        left = tk.Frame(main, bg="#1e1e1e", width=280)
        left.pack(side="left", fill="y")

        right = tk.Frame(main, bg="#121212")
        right.pack(side="right", fill="both", expand=True)

        # ================= LEFT PANEL =================

        self.action = tk.IntVar(value=0)

        tk.Label(left, text="Select Action",
                 fg="white", bg="#1e1e1e").pack(pady=10)

        tk.Radiobutton(left, text="0 - Safe",
                       variable=self.action, value=0,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        tk.Radiobutton(left, text="1 - Notify",
                       variable=self.action, value=1,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        tk.Radiobutton(left, text="2 - Alarm",
                       variable=self.action, value=2,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        tk.Radiobutton(left, text="3 - Emergency",
                       variable=self.action, value=3,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        # -------- Face Registration --------
        tk.Button(left, text="📸 Register Face",
                  command=self.register_user).pack()

        # -------- Face Recognition --------
        tk.Button(left, text="👁 Start Recognition",
                  command=lambda: threading.Thread(target=self.start_recognition).start()
                  ).pack()

        tk.Button(left, text="🛑 Stop System",
                  width=25, command=self.stop_system).pack(pady=5)

        # -------- Mode Selection --------
        tk.Label(left, text="Select Mode",
                 fg="white", bg="#1e1e1e").pack(pady=10)

        tk.Radiobutton(left, text="🛡 Protector Mode",
                       variable=self.mode, value="PROTECTOR",
                       command=self.update_mode,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        tk.Radiobutton(left, text="🔥 Defender Mode",
                       variable=self.mode, value="DEFENDER",
                       command=self.update_mode,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        tk.Radiobutton(left, text="🛑 Stop Mode",
                       variable=self.mode, value="STOP",
                       command=self.update_mode,
                       bg="#1e1e1e", fg="white").pack(anchor="w")

        # -------- Trigger --------
        tk.Button(left, text="⚡ Simulate Intruder",
                  width=25, command=self.trigger_alert).pack(pady=20)

        # ================= RIGHT PANEL =================

        status_frame = tk.Frame(right, bg="#1e1e1e", height=100)
        status_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(status_frame, text="System Status",
                 fg="white", bg="#1e1e1e",
                 font=("Arial", 12, "bold")).pack(anchor="w")

        self.status_label = tk.Label(status_frame,
                                     text="System Idle",
                                     fg="lime", bg="#1e1e1e")
        self.status_label.pack(anchor="w")

        tk.Label(right, text="Live Logs",
                 fg="white", bg="#121212",
                 font=("Arial", 12, "bold")).pack(anchor="w", padx=10)

        self.log_box = scrolledtext.ScrolledText(
            right, height=20, bg="black", fg="lime")
        self.log_box.pack(fill="both", expand=True, padx=10, pady=10)

    # ================= LOG FUNCTION =================
    def log(self, text):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.yview(tk.END)

    def update_mode(self):
        self.log(f"🔄 Mode changed to: {self.mode.get()}")

    def update_action(self):
        action = self.action.get()
        self.log(f"🎯 Action changed to: {action}")

    # ================= FEATURES =================

    def register_user(self):
        name = simpledialog.askstring("Register Face", "Enter name:")
        if name:
            self.log(f"📸 Registering {name}...")
            register_face(name)
            self.log(f"✅ {name} registered")

    def start_recognition(self):

        if self.mode.get() == "STOP":
            self.log("⚠ System is stopped")
            return

        self.log("📡 Starting recognition...")
        self.status_label.config(text="Scanning...")

        person_type, name = recognize_person()

        # ================= RL PIPELINE =================

        face_result = True if person_type == "KNOWN" else False
        hour = datetime.now().hour

        if not face_result:
            self.attempts += 1
        else:
            self.attempts = 0

        state = get_state(
            face_result,
            0.5,  # simulated confidence
            self.attempts,
            hour,
            self.mode.get().lower()
        )

        self.log(f"STATE: {state}")

        action = decide_action(state)

        self.log(f"AI ACTION: {ACTIONS[action]}")

        # ================= EXECUTE =================
        self.alert.execute(action, self.mode.get().upper())

        self.log("⚡ Alert system triggered")

        # ================= UI STATUS =================

        if face_result:
            self.log(f"✅ Authorized: {name}")
            self.status_label.config(text=f"Authorized: {name}")
        else:
            self.log("🚨 UNKNOWN DETECTED")
            self.status_label.config(text="Intruder Detected 🚨")

    def stop_system(self):
        self.status_label.config(text="System Stopped")
        self.log("🛑 System stopped")

    def simulate_alert(self):
        action = self.action.get()
        mode = self.mode.get()
        self.log(f"⚡ Simulating → Action: {action}, Mode: {mode}")
        self.alert.execute(action, mode)

    def trigger_alert(self):
        mode = self.mode.get()
        action = self.action.get()

        if mode == "STOP":
            self.log("⚠ System is stopped")
            return

        self.log(f"⚡ Simulating Intruder → Mode: {mode}, Action: {action}")
        self.status_label.config(text="Simulating Alert...")
        self.alert.execute(action, mode)
        self.log("✅ Simulation complete")


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()