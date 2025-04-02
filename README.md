# Upload and Detect: AI Smart Object Detection in Video - Ultralytics YOLOv8 -Streamlit and Python

Detect objects in your uploaded videos using YOLOv8 and Streamlit. This app allows users to process videos and identify objects in real-time. You can upload MP4, AVI, MOV, MPEG4 videos.

# Installation Instructions

1. Clone the Repository
git clone https://github.com/ErikElcsics/Upload-and-Detect-AI-Smart-Object-Detection-in-Video-Ultralytics-YOLOv8-Streamlit-Python.git

cd your-repo

2. Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required libraries:

- Streamlit 
- OpenCV 
- Ultralytics YOLOv8 
- Torch 

3. Install YOLOv8 Weights
Download the YOLOv8 model weights and place them in the Yolo-Weights folder:

mkdir -p Yolo-Weights
wget -P Yolo-Weights https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt

# How to Use app

Run the Streamlit App:

1. Streamlit run app.py
2. Upload any video and wait for processing to complete.
3. Download the processed video with detected objects.
4. View the processed video

# Libraries Used
- Streamlit → For the user interface
- OpenCV → For video processing
- Ultralytics YOLOv8 → For object detection
- Torch → For running the YOLO model
- NumPy
- Os

# About Streamlit & YOLO:

Streamlit
Streamlit is a fast and easy-to-use Python framework for building web applications. It simplifies UI development, allowing interactive apps with minimal code.

Ultralytics YOLOv8
YOLO (You Only Look Once) is a real-time object detection model known for its speed and accuracy. YOLOv8 by Ultralytics enhances previous versions with better accuracy, efficiency, and ease of use.

YOLOv8 Model Used
This app uses YOLOv8-Large (yolov8l.pt), a high-performance model that balances speed and detection accuracy. It is trained on the COCO dataset, recognizing 80+ object classes, including people, vehicles, animals, and everyday objects.

# License
This project is licensed under the MIT License.

![image](https://github.com/user-attachments/assets/1b741da8-6302-4dd5-b342-0a753f56695e)

![image](https://github.com/user-attachments/assets/1ea8fb96-c951-4fc7-80a4-43b4a16dacb4)

![image](https://github.com/user-attachments/assets/b96d8490-8a4a-4367-9592-2bf4c238a717)

![image](https://github.com/user-attachments/assets/4a923e6c-f92a-4497-878c-7759565558d3)

Few more examples of a Processed Detected Videos.

![image](https://github.com/user-attachments/assets/277e5dd7-2383-436f-b3c9-ab12903ff899)

![image](https://github.com/user-attachments/assets/701d1707-7dbc-48c3-938a-77d82f3c44c0)

![image](https://github.com/user-attachments/assets/8271a785-0066-4997-bca3-7b66b8dffed4)




