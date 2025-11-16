"""
YOLO Pose Estimation
- Use pre-trained YOLO pose detection models (yolov8n-pose.pt or yolo11n-pose.pt)
- Detect human poses in real-time webcam feed
- Display keypoints and skeleton connections
"""

import cv2
from ultralytics import YOLO

# Load YOLO Pose model
print("Loading YOLO Pose model...")
print("Trying to load yolov8n-pose.pt...")

try:
    model = YOLO("yolov8n-pose.pt")
    print("Successfully loaded yolov8n-pose.pt")
except Exception as e:
    print(f"Could not load yolov8n-pose.pt: {e}")
    print("Trying yolo11n-pose.pt...")
    try:
        model = YOLO("yolo11n-pose.pt")
        print("Successfully loaded yolo11n-pose.pt")
    except Exception as e2:
        print(f"Could not load yolo11n-pose.pt: {e2}")
        print("Please ensure you have a YOLO pose model available.")
        exit()

print("\n" + "="*60)
print("YOLO POSE ESTIMATION")
print("="*60)
print("This model detects human poses with keypoints including:")
print("- Head (nose, eyes, ears)")
print("- Upper body (shoulders, elbows, wrists)")
print("- Lower body (hips, knees, ankles)")
print("\nKeypoints are connected to show the human skeleton.")
print("="*60 + "\n")

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Webcam opened successfully!")
print("\nControls:")
print("  Press 'q' - Quit")
print("  Press 'c' - Toggle confidence threshold display")
print("="*60 + "\n")

show_confidence = True

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    # Run YOLO pose estimation
    results = model(frame, verbose=False)

    # Annotate frame with pose keypoints and skeleton
    annotated_frame = results[0].plot()

    # Get pose information
    if results[0].keypoints is not None:
        num_poses = len(results[0].keypoints)
        cv2.putText(annotated_frame, f"Poses Detected: {num_poses}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    else:
        cv2.putText(annotated_frame, "No poses detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Add instructions
    cv2.putText(annotated_frame, "Press 'q' to quit | 'c' to toggle confidence",
                (10, annotated_frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("YOLO Pose Estimation", annotated_frame)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Exiting...")
        break
    elif key == ord('c'):
        show_confidence = not show_confidence
        print(f"Confidence display: {'ON' if show_confidence else 'OFF'}")

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Program ended.")
print("\nPose estimation completed successfully!")
