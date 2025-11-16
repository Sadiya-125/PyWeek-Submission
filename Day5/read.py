# py -3.11 read.py

import cv2

# # IMAGE READING
# image=cv2.imread('image.jpg')
# # gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# resized = cv2.resize(image, (700,700))
# blur = cv2.GaussianBlur(resized, (7,7), 3)
# cv2.imshow('VIRAT KOHLI', blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# VIDEO READING
cap=cv2.VideoCapture(1)
while True:
    success,frame=cap.read()
    cv2.flip(frame,1,frame)
    if not success:
        break
    cv2.imshow('My Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
