import streamlit as st
import cv2
import tempfile
import torch
from ultralytics import YOLO
import os
import numpy as np

# Load YOLO model
model = YOLO("../Yolo-Weights/yolov8l.pt")

# Streamlit UI
st.title("🎥 Upload and Detect: AI Smart Object Detection in Video")
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])]
                confidence = box.conf[0].item()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.read())
        temp_video_path = temp_video.name

    output_video_path = temp_video_path.replace(".mp4", "_detected.mp4")

    # Display original video
    st.subheader("Original Video")
    st.video(temp_video_path)

    if st.button("Process Video"):
        with st.spinner("Detecting objects..."):
            process_video(temp_video_path, output_video_path)
        st.success("Processing complete! You can now download the detected video to view it.")

        # Download button (No processed video preview)
        with open(output_video_path, "rb") as processed_file:
            st.download_button("Download Processed Video", processed_file, file_name="detected_video.mp4", mime="video/mp4")
