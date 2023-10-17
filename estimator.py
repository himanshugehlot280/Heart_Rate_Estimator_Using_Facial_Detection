import streamlit as st
import cv2
import numpy as np
import time


def estimate_heart_rate(face_frames, fps):
    # Calculate the average green channel intensity in each frame
    green_intensities = []
    for frame in face_frames:
        green_channel = frame[:, 1]  # Green channel is index 1 in OpenCV
        green_intensity = np.mean(green_channel)
        green_intensities.append(green_intensity)

    # Compute the FFT of the green intensities
    fft = np.fft.fft(green_intensities)
    freqs = np.fft.fftfreq(len(fft), d=1 / fps)
    magnitudes = np.abs(fft)

    # Find the frequency with the highest magnitude in a reasonable heart rate range
    min_freq = 0.6  # Minimum heart rate frequency (beats per second)
    max_freq = 3.0  # Maximum heart rate frequency (beats per second)
    valid_freqs = np.where((freqs >= min_freq) & (freqs <= max_freq))
    dominant_freq_index = np.argmax(magnitudes[valid_freqs])
    dominant_freq = freqs[valid_freqs][dominant_freq_index]

    # Convert dominant frequency to heart rate (beats per minute)
    heart_rate_bpm = dominant_freq * 60

    return abs(heart_rate_bpm)


def detect_faces(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces


# def detect_forehead(frame):
#     # Load the pre-trained face detection classifier
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     # Convert the frame to grayscale for face detection
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Perform face detection
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     if len(faces) > 0:
#         x, y, w, h = faces[0]  # Assuming only one face is detected
#         forehead_y = y + int(0.2 * h)  # Adjust this value based on your desired forehead height
#         forehead_frame = frame[forehead_y:y+h, x:x+w]
#         return forehead_frame
#     else:
#         return None

# def generate_bpm_value(heart_rate):
#     # Generate example BPM data
#     # time = np.linspace(0, 60, num=100)  # Time in seconds
#     bpm_values = heart_rate  # Example BPM values
#     # Create a DataFrame with time and BPM values
#     bpm_data = {'BPM': bpm_values}
#     st.line_chart(bpm_data, use_container_width=True)
#     return bpm_data


def main():
    st.title("Heart Rate Estimation using Live Facial Detection")

    cap = cv2.VideoCapture(0)  # Open the webcam

    stframe = st.empty()
    stop_button = st.button("Stop Estimation")

    while not stop_button:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces
        faces = detect_faces(frame)

        # Process each detected face
        for (x, y, w, h) in faces:
            face_frame = frame[y:y + h, x:x + w]

            # Estimate heart rate for the face
            fps = 30
            estimated_heart_rate = estimate_heart_rate(face_frame, fps)

            # Display the frame with bounding box and estimated heart rate
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Heart Rate: {estimated_heart_rate}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 255, 0), 2)

            # forehead_frame = detect_forehead(frame)

            # if forehead_frame is not None:
            #     cv2.imshow("Forehead Region", forehead_frame)

            # chart = st.line_chart([])
            # while True:
            #     bpm_value = generate_bpm_value(estimated_heart_rate)
            #     chart.add_rows([bpm_value])
            #     time.sleep(1)

        # Display the captured frame
        stframe.image(frame, channels="BGR", caption="Live Facial Detection", use_column_width=True)

    # Release the webcam
    cap.release()


if __name__ == "__main__":
    main()

