import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Drawing specs for landmarks
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Start webcam
cap = cv2.VideoCapture(1)

# Function to calculate Euclidean distance
def euclidean(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

with mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        mood = "Detecting..."

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Get landmark points (mouth corners, eyes, eyebrows)
                h, w, _ = frame.shape
                landmarks = [(int(l.x * w), int(l.y * h)) for l in face_landmarks.landmark]

                # Key points for expression detection
                left_mouth = landmarks[61]
                right_mouth = landmarks[291]
                top_lip = landmarks[13]
                bottom_lip = landmarks[14]
                left_eyebrow = landmarks[70]
                right_eyebrow = landmarks[300]
                nose_tip = landmarks[1]

                # Calculate distances
                mouth_width = euclidean(left_mouth, right_mouth)
                mouth_open = euclidean(top_lip, bottom_lip)
                eyebrow_dist = euclidean(left_eyebrow, right_eyebrow)

                # Basic logic for mood detection
                if mouth_open > 25:
                    mood = "😮 Surprised"
                elif mouth_width > 60:
                    mood = "😊 Happy"
                elif mouth_width < 30:
                    mood = "😠 Angry"
                else:
                    mood = "😐 Neutral"

                # Draw the face mesh
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec,
                )

        # Display mood text
        cv2.putText(frame, f'Mood: {mood}', (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

        cv2.imshow("AI Mood Mirror", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
