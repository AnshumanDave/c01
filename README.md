Hand Detection with MediaPipe
=============================

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- NumPy (`pip install numpy`)

## How to Run
1. Ensure you have the required libraries installed.
2. Save the Python script (`hand_detection.py`) in your working directory.
3. Connect a webcam to your computer.
4. Run the script: python hand-detection.py
5. A window will display the webcam feed:
- The hand skeleton is drawn over detected hands.
- A red circle is drawn on the index fingertip.
- The terminal prints "Pinching" or "Not Pinching" based on the distance between the thumb and index fingertips.
6. Press 'q' to exit.

## Notes
- Ensure adequate lighting for better hand detection.
- The "Pinching" feature detects when the thumb and index fingertip are less than 40 pixels apart.

