import cv2
import ultralytics
from ultralytics import YOLO

model =YOLO('yolo11n.pt')
cap=cv2.VideoCapture(1)
while True:
    success,frame=cap.read()
    cv2.flip(frame,1,frame)
    if not success:
        break
    results=model(frame)
    annotated_frame=results[0].plot()
    gray=cv2.cvtColor(annotated_frame,cv2.COLOR_BGR2RGB)
    blur=cv2.GaussianBlur(gray,(7,7),3)
    cv2.imshow("OBJECT DETECTION", blur)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


