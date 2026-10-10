# YOLOv8-World Object Detection 🚀

## 📌 Overview

This project uses Computer Vision and the YOLOv8-World model (`yolov8s-world.pt`) to detect objects in images and videos.

YOLOv8-World supports open-vocabulary object detection, allowing users to specify objects using text prompts.

## ✨ Features

- Object detection using YOLOv8-World
- Image and video detection
- Customizable object classes
- Bounding boxes around detected objects
- Confidence scores for predictions
- Built with Python and OpenCV

## 🛠️ Technologies Used

- Python
- Computer Vision
- YOLOv8-World
- Ultralytics
- OpenCV

## 💻 Code Example

```python
from ultralytics import YOLOWorld

# Load the pretrained model
model = YOLOWorld("yolov8s-world.pt")

# Specify objects to detect
model.set_classes(["person", "car", "bicycle", "dog"])

# Detect objects in an image
results = model.predict(
    source="image.jpg",
    conf=0.25,
    show=True
)
```

## 🎯 Applications

- Drone-based object detection
- Smart surveillance
- Traffic monitoring
- Robotics and autonomous systems
- Industrial inspection

## 🚀 Future Improvements

- Real-time webcam detection
- Video analytics
- Drone camera integration
- FastAPI deployment

## 👨‍💻 Author

**M Arshad**

Artificial Intelligence Student | Computer Vision | Deep Learning | Robotics

## 📄 License

For educational and research purposes. Review the applicable model and dependency licenses before commercial use.
