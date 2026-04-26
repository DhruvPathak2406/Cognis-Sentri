from DecisionEngine.state import get_state
from DecisionEngine.learning import train
from DecisionEngine.agent import decide_action, ACTIONS

from recognition_module.interface import recognize_face

from datetime import datetime
import time

# -------------------------------
# TRAIN MODEL (once)
# -------------------------------
train(5000)

# -------------------------------
# LOOP
# -------------------------------
attempts = 0
mode = "protector"

while True:

    # 1. RECOGNITION
    face_result, confidence = recognize_face()

    # 2. TIME (real now)
    hour = datetime.now().hour

    # 3. ATTEMPTS LOGIC
    if not face_result:
        attempts += 1
    else:
        attempts = 0

    # 4. STATE
    state = get_state(face_result, confidence, attempts, hour, mode)

    print("\nSTATE:", state)

    # 5. DECISION
    action = decide_action(state)

    print("ACTION:", ACTIONS[action])

    # 6. DELAY
    time.sleep(2)