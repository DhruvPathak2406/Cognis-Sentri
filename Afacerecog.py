import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from deepface import DeepFace
import cv2
import time

cap = cv2.VideoCapture(0)

max_attempts = 20
required_matches = 4

attempt = 0
match_count = 0
person_name = "UNKNOWN"

print("Scanning face with verification...")

while attempt < max_attempts:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="faces",
            enforce_detection=False,
            silent=True
        )

        if len(result[0]) > 0:
            identity = result[0]['identity'][0]
            name = identity.split("\\")[-1].split(".")[0]

            match_count += 1
            person_name = name

            print(f"Match {match_count}/{required_matches}: {name}")

            # Stop early if enough matches
            if match_count >= required_matches:
                print("✅ VERIFIED")
                break
        else:
            print(f"Attempt {attempt+1}: Unknown")

    except:
        print("Face not detected")

    attempt += 1
    time.sleep(0.3)

    cv2.imshow("Scanning...", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Final decision
if match_count >= required_matches:
    print(f"🎯 FINAL RESULT: VERIFIED ({person_name})")
else:
    print("🚨 FINAL RESULT: UNKNOWN 🚨")

cap.release()
cv2.destroyAllWindows()