import cv2
import numpy as np
import mediapipe as mp


#Drawing on a Black Canvas with Webcam Feed (continuous lines, pause & erase)
cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
canvas = None

drawing_enabled = True      # toggle drawing on/off
eraser_mode = False         # toggle eraser on/off
draw_color = (255, 0, 255)
draw_radius = 15

prev_point = None  # store previous (x,y) for continuous lines

while True:
    success, img = cap.read()
    cv2.flip(img, 1, img)  # Mirror the image
    if not success:
        break

    if canvas is None:
        canvas = np.zeros_like(img)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Default gesture state
    fingers_up = 0

    if results.multi_hand_landmarks:
        handLms = results.multi_hand_landmarks[0]  # use first detected hand
        h, w, c = img.shape

        # Count fingers (exclude thumb for simplicity)
        tips = [8, 12, 16, 20]
        for tip in tips:
            if handLms.landmark[tip].y < handLms.landmark[tip - 2].y:
                fingers_up += 1

        # Gesture controls:
        # - 1 finger (index) => draw
        # - 2 fingers => pause (stop drawing)
        # - 5 fingers => clear/erase canvas
        if fingers_up == 1:
            drawing_enabled = True
        elif fingers_up == 2:
            drawing_enabled = False
        elif fingers_up == 4:  # depending on detection, 4 means all four non-thumb fingers up
            canvas = np.zeros_like(img)
            prev_point = None

        # Draw using index fingertip as continuous line
        idx_lm = handLms.landmark[8]
        cx, cy = int(idx_lm.x * w), int(idx_lm.y * h)

        if drawing_enabled and fingers_up == 1:
            color = (0, 0, 0) if eraser_mode else draw_color
            thickness = draw_radius * (2 if eraser_mode else 1)
            if prev_point is None:
                prev_point = (cx, cy)
            # draw line from previous point to current
            cv2.line(canvas, prev_point, (cx, cy), color, thickness)
            prev_point = (cx, cy)
        else:
            # reset previous point when not drawing to avoid jumps
            prev_point = None

        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    else:
        prev_point = None  # no hand detected, reset

    # Overlay status and instructions
    status = "Paused" if not drawing_enabled else ("Eraser" if eraser_mode else "Drawing")
    cv2.putText(img, f"Mode: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, "Gestures: 1=index draw | 2=pause | 5=open palm clear", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    cv2.putText(img, "Keys: p=toggle pause | e=toggle eraser | c=clear | q=quit", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    combined = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
    cv2.imshow("Webcam with Drawing", combined)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('p'):
        drawing_enabled = not drawing_enabled
        prev_point = None
    elif key == ord('e'):
        eraser_mode = not eraser_mode
    elif key == ord('c'):
        canvas = np.zeros_like(img)
        prev_point = None

cap.release()
cv2.destroyAllWindows()