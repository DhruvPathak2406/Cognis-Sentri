import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from deepface import DeepFace
import cv2
import time
def recognize_person():
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
        result = None  # always define

        try:
            result = DeepFace.find(
                img_path=frame,
                db_path="faces",
                enforce_detection=False,
                silent=True
            )
        except:
            result = None
        # ✅ SAFE CHECK
        if result is not None and len(result[0]) > 0:
            distance = result[0]['distance'][0]
            if distance < 0.4:   # confidence threshold
                identity = result[0]['identity'][0]
                name = identity.split("\\")[-1].split(".")[0]
                match_count += 1
                person_name = name
                print(f"Match {match_count}/{required_matches}: {name}")
                if match_count >= required_matches:
                    print("✅ VERIFIED")
                    break
        else:
            print(f"Attempt {attempt+1}: Unknown")
        attempt += 1
        time.sleep(0.3)
        cv2.imshow("Scanning...", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    # ✅ FINAL OUTPUT
    if match_count >= required_matches:
        return "KNOWN", person_name
    else:
        return "UNKNOWN", None