"""
YOLO Object Detection with Class Filtering
- Load YOLO model and print all available classes
- Filter detection to specific classes
- Demonstrate detection for different class combinations
"""

import cv2
from ultralytics import YOLO

# Load YOLO model
print("Loading YOLO model...")
model = YOLO("yolo11n.pt")

# Print all available classes
print("\n" + "="*60)
print("AVAILABLE OBJECT CLASSES IN YOLO MODEL")
print("="*60)
print(model.names)
print("\nTotal classes:", len(model.names))
print("="*60)

# Display classes in a readable format
print("\nClass ID -> Class Name mapping:")
for class_id, class_name in model.names.items():
    print(f"  {class_id:2d}: {class_name}")

print("\n" + "="*60)
print("INSTRUCTIONS:")
print("Press number keys to filter different classes:")
print("  '0' - Person only")
print("  '1' - Bicycle only")
print("  '2' - Car only")
print("  '3' - Motorcycle only")
print("  '4' - Airplane only")
print("  '5' - Bus only")
print("  '6' - Train only")
print("  '7' - Truck only")
print("  '8' - Boat only")
print("  'a' - All classes")
print("  'p' - Person, Car, Bicycle (common objects)")
print("  'v' - All vehicles (car, truck, bus, motorcycle)")
print("  'q' - Quit")
print("="*60 + "\n")

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Default: detect only person (class 0)
current_classes = [0]
filter_mode = "Person only"

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    # Run YOLO detection with class filtering
    results = model(frame, classes=current_classes, verbose=False)

    # Annotate frame with detection results
    annotated_frame = results[0].plot()

    # Add overlay information
    cv2.putText(annotated_frame, f"Filter Mode: {filter_mode}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"Classes: {current_classes}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    cv2.putText(annotated_frame, "Press 0-8 for specific class | 'a' for all | 'q' to quit",
                (10, annotated_frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("YOLO Object Detection with Class Filtering", annotated_frame)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Exiting...")
        break
    elif key == ord('0'):
        current_classes = [0]
        filter_mode = "Person only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('1'):
        current_classes = [1]
        filter_mode = "Bicycle only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('2'):
        current_classes = [2]
        filter_mode = "Car only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('3'):
        current_classes = [3]
        filter_mode = "Motorcycle only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('4'):
        current_classes = [4]
        filter_mode = "Airplane only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('5'):
        current_classes = [5]
        filter_mode = "Bus only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('6'):
        current_classes = [6]
        filter_mode = "Train only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('7'):
        current_classes = [7]
        filter_mode = "Truck only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('8'):
        current_classes = [8]
        filter_mode = "Boat only"
        print(f"Filtering: {filter_mode}")
    elif key == ord('a'):
        current_classes = None  # None means all classes
        filter_mode = "All classes"
        print(f"Filtering: {filter_mode}")
    elif key == ord('p'):
        current_classes = [0, 1, 2]  # Person, bicycle, car
        filter_mode = "Person, Bicycle, Car"
        print(f"Filtering: {filter_mode}")
    elif key == ord('v'):
        current_classes = [2, 3, 5, 7]  # Car, motorcycle, bus, truck
        filter_mode = "All vehicles"
        print(f"Filtering: {filter_mode}")

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Program ended.")
