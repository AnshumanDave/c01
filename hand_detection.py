import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame
    success, frame = cap.read()
    if not success:
        continue

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection
    result = hands.process(frame_rgb)

    # Check if any hand landmarks are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw the hand skeleton
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark points
            h, w, _ = frame.shape
            landmarks = hand_landmarks.landmark

            # Calculate coordinates for index finger tip and thumb tip
            index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
            thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))

            # Draw red circle on the index fingertip
            cv2.circle(frame, index_tip, 10, (0, 0, 255), -1)

            # Calculate Euclidean distance between thumb and index finger
            distance = np.linalg.norm(np.array(index_tip) - np.array(thumb_tip))

            # Print pinching status
            if distance < 40:
                print("Pinching")
            else:
                print("Not Pinching")

    # Display the frame
    cv2.imshow("Hand Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
