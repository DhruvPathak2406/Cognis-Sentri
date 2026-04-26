import cv2
import os
import time

def register_face(name):
    path = f"faces/{name}"
    os.makedirs(path, exist_ok=True)

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 🔥 specify backend for better compatibility

    if not cam.isOpened():
        print("Camera error")
        return

    print(f"📸 Registering {name}...")

    # 🔥 ADD: face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # 🔥 ADD: prep time
    print("⏳ Get ready... capturing starts in 3 seconds")
    time.sleep(3)

    count = 0

    while count < 15:
        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # 🔥 ADD: convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 🔥 ADD: detect face
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # 🔥 ADD: draw rectangle (visual feedback)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Registering Face", frame)

        # 🔥 CHANGE: only capture if face detected
        if len(faces) > 0:
            img_path = f"{path}/{count}.jpg"
            cv2.imwrite(img_path, frame)

            print(f"✅ Saved {img_path}")

            count += 1

            time.sleep(0.7)  # 🔥 better spacing (was 0.5)

        # exit option
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    print(f"✅ {name} registered successfully")