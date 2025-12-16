# HSV-Based Red Color Detection with OpenCV

This project demonstrates basic red color detection using the HSV color space
with Python and OpenCV.

## 📌 Project Overview
- BGR to HSV color space conversion
- Red color range definition
- Mask generation using `cv2.inRange`
- Visual output of detection results

## 🛠 Technologies Used
- Python
- OpenCV
- NumPy

## 📷 Sample Output

### Original Image
![Original](screenshots/original.png)

### Red Color Mask
![Mask](screenshots/mask.png)

## 🚀 Use Case
This is a fundamental step for:
- Computer vision applications
- UAV target detection systems
- Image processing pipelines

## 📂 How to Run
```bash
pip install opencv-python numpy
python red_color_detection.py
