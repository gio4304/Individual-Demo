import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# Load model exported from Teachable Machine
model = tf.keras.models.load_model(r"C:\Users\ababb\OneDrive\Documents\School Project\v1\keras_model.h5")

# Open labels file
with open(r"C:\Users\ababb\OneDrive\Documents\School Project\v1\labels.txt", "r") as f:
    labels = f.read().splitlines()

# Serial port for Arduino Mega 2560
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Preprocess image
    img = cv2.resize(frame, (224, 224)).astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(img)
    index = np.argmax(prediction)
    label = labels[index]

    print("Detected:", label)

    # Send to Mega 2560
    arduino.write((label + "\n").encode())

    # Show webcam feed
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
