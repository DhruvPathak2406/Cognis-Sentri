import cv2
import os
import numpy as np

name = input("Enter person name: ")
path = f"faces/{name}"

os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Camera not working")
    exit()

count = 0
data = []

print("Press 'c' to capture images")

while count < 15:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Capture", frame)

    key = cv2.waitKey(1)

    if key == ord('c'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (100, 100))

        # Save image
        cv2.imwrite(f"{path}/{count}.jpg", frame)

        # Store flattened data
        data.append(resized.flatten())

        print(f"Image {count} saved")
        count += 1

    elif key == 27:
        break

cam.release()
cv2.destroyAllWindows()

# Convert to numpy
data = np.array(data)

# Save
np.save(f"{name}_data.npy", data)

print("Face registration complete")