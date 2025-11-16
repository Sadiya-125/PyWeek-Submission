"""
Real-time Webcam with Gaussian Blur and Color Conversions
- Apply Gaussian Blur to webcam feed
- Demonstrate different color space conversions in real-time
"""

import cv2
import numpy as np

# Initialize webcam (0 for default, 1 for external webcam)
cap = cv2.VideoCapture(1)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Webcam opened successfully!")
print("Controls:")
print("  Press '1' - Original feed")
print("  Press '2' - Grayscale")
print("  Press '3' - HSV")
print("  Press '4' - LAB")
print("  Press '5' - YCrCb")
print("  Press 'b' - Toggle Gaussian Blur")
print("  Press 'q' - Quit")

# Variables
blur_enabled = False
current_mode = 1  # 1=Original, 2=Gray, 3=HSV, 4=LAB, 5=YCrCb
kernel_size = (15, 15)  # Gaussian blur kernel size

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    # Apply Gaussian Blur if enabled
    if blur_enabled:
        frame = cv2.GaussianBlur(frame, kernel_size, 0)

    # Apply color conversion based on current mode
    if current_mode == 1:
        display_frame = frame.copy()
        mode_text = "Original"
    elif current_mode == 2:
        # Grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
        mode_text = "Grayscale (COLOR_BGR2GRAY)"
    elif current_mode == 3:
        # HSV
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mode_text = "HSV (COLOR_BGR2HSV)"
    elif current_mode == 4:
        # LAB
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        mode_text = "LAB (COLOR_BGR2LAB)"
    elif current_mode == 5:
        # YCrCb
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        mode_text = "YCrCb (COLOR_BGR2YCrCb)"

    # Add text overlay
    blur_status = "ON" if blur_enabled else "OFF"
    cv2.putText(display_frame, f"Mode: {mode_text}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(display_frame, f"Gaussian Blur: {blur_status}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(display_frame, "Press 1-5 to change mode | 'b' for blur | 'q' to quit",
                (10, display_frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("Webcam - Gaussian Blur & Color Conversions", display_frame)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Exiting...")
        break
    elif key == ord('1'):
        current_mode = 1
        print("Switched to Original mode")
    elif key == ord('2'):
        current_mode = 2
        print("Switched to Grayscale mode")
    elif key == ord('3'):
        current_mode = 3
        print("Switched to HSV mode")
    elif key == ord('4'):
        current_mode = 4
        print("Switched to LAB mode")
    elif key == ord('5'):
        current_mode = 5
        print("Switched to YCrCb mode")
    elif key == ord('b'):
        blur_enabled = not blur_enabled
        print(f"Gaussian Blur: {'ON' if blur_enabled else 'OFF'}")

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Webcam released and windows closed.")
