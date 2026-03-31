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

                if match_count >= required_matches:
                    break

        except:
            pass

        attempt += 1
        time.sleep(0.3)

    cap.release()
    cv2.destroyAllWindows()

    # ✅ RETURN MUST BE INSIDE FUNCTION
    if match_count >= required_matches:
        return "KNOWN", person_name
    else:
        return "UNKNOWN", None