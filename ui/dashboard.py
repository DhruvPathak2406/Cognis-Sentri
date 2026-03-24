import tkinter as tk
from tkinter import scrolledtext
from turtle import left, mode
from alert_module.alert import AlertSystem


class Dashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Cognis-Sentri AI Security System")
        self.root.geometry("1000x650")
        self.root.configure(bg="#121212")
        self.alert = AlertSystem()
        self.mode = tk.StringVar(value="STOP")

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
                  width=25, command=self.fake_register).pack(pady=5)

        # -------- Face Recognition --------
        tk.Button(left, text="👁 Start Recognition",
                  width=25, command=self.fake_recognition).pack(pady=5)

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

        # -------- STATUS PANEL --------
        status_frame = tk.Frame(right, bg="#1e1e1e", height=100)
        status_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(status_frame, text="System Status",
                 fg="white", bg="#1e1e1e",
                 font=("Arial", 12, "bold")).pack(anchor="w")

        self.status_label = tk.Label(status_frame,
                                     text="System Idle",
                                     fg="lime", bg="#1e1e1e")
        self.status_label.pack(anchor="w")

        # -------- LOG PANEL --------
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
      mode = self.mode.get()
      self.log(f"🔄 Mode changed to: {mode}")
      
    def update_action(self):
       action = self.action.get()
       self.log(f"🎯 Action changed to: {action}")

    # ================= PLACEHOLDER FEATURES =================

    def fake_register(self):
        self.status_label.config(text="Face Registration Module Ready")
        self.log("📸 Face Registration UI triggered (module not connected yet)")

    def fake_recognition(self):
        self.status_label.config(text="Recognition Module Ready")
        self.log("👁 Recognition system initialized (not connected yet)")

    def stop_system(self):
        self.status_label.config(text="System Stopped")
        self.log("🛑 System stopped")

    # ================= REAL ALERT SYSTEM =================

    def trigger_alert(self):

        mode = self.mode.get()
        action = self.action.get()

        self.log(f"⚙ Mode selected: {mode}")
        self.log(f"🎯 Action selected: {action}")

        if mode == "STOP":
           self.log("⚠ System is stopped")
           return

        self.status_label.config(text="Processing Event...")
        self.alert.execute(action, mode)
        self.log("✅ Alert executed")


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()