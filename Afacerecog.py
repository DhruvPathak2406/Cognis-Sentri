import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings
from alert_module.alert import send_telegram, log_event     
from deepface import DeepFace
import cv2
import time

def recognize_person():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Same camera as registration
    if not cap.isOpened():
        print("❌ Camera not opening")
        return "UNKNOWN", None

    max_attempts = 20
    required_matches = 3   # Logic: 3 consistent matches for verification
    attempt = 0
    match_count = 0
    person_name = "UNKNOWN"

    print("Scanning face with verification...")

    while attempt < max_attempts:
        ret, frame = cap.read()
        if not ret:
            break

        result = None
        try:
            # Searching for the face in the local 'faces' database
            result = DeepFace.find(
                img_path=frame,
                db_path="faces",
                enforce_detection=False,
                silent=True
            )
        except Exception as e:
            result = None

        if result and len(result) > 0 and not result[0].empty:
            distance = result[0]['distance'][0]
            
            # Threshold check: lower is more similar. 0.65 is a good balance.
            if distance < 0.5:   
                identity = result[0]['identity'][0]
                
                # Extracting folder name from path (e.g., 'faces\John\img1.jpg' -> 'John')
                # Using os.path.sep for cross-platform compatibility
                path_parts = identity.split(os.sep)
                name = path_parts[-2] 
                
                match_count += 1
                person_name = name
                print(f"Match {match_count}/{required_matches}: {name} (Dist: {distance:.4f})")

                if match_count >= required_matches:
                    print("✅ VERIFIED")
                    break
        else:
            print(f"Attempt {attempt+1}: No match found")

        attempt += 1
        cv2.imshow("Scanning...", frame)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        time.sleep(0.1) # Short delay to allow for clear frames

    cap.release()
    cv2.destroyAllWindows()

    # Final Result Logic
    if match_count >= required_matches:
        return "KNOWN", person_name
    else:
        return "UNKNOWN", None

# --- Execution and Output ---
if __name__ == "__main__":
    status, name = recognize_person()

    print("\n" + "="*30)
    if status == "KNOWN":
        print(f"RESULT: Access Granted")
        print(f"PERSON: {name}")
    else:
        print("RESULT: Access Denied")
        print("PERSON: Unknown / Not Verified")
    print("="*30)