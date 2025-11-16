"""
Image Manipulation Homework
- cv2.resize() to scale image to 1/4 of window size
- cv2.cvtColor() with at least 3 different color conversions
"""

import cv2
import numpy as np

img = cv2.imread('image.jpg')

print(f"Original image shape: {img.shape}")

# Task 1: Resize to 1/4 of the original size
height, width = img.shape[:2]
new_width = width // 4
new_height = height // 4
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
print(f"Resized image shape (1/4 size): {resized_img.shape}")

# Task 2: Apply at least 3 different color conversions
# Conversion 1: BGR to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Grayscale conversion: COLOR_BGR2GRAY - Shape: {gray_img.shape}")

# Conversion 2: BGR to HSV (Hue, Saturation, Value)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(f"HSV conversion: COLOR_BGR2HSV - Shape: {hsv_img.shape}")

# Conversion 3: BGR to LAB (L*a*b color space)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
print(f"LAB conversion: COLOR_BGR2LAB - Shape: {lab_img.shape}")

# Conversion 4: BGR to YCrCb (Luma, Red-difference, Blue-difference)
ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
print(f"YCrCb conversion: COLOR_BGR2YCrCb - Shape: {ycrcb_img.shape}")

# Display all images
cv2.imshow("Original Image", img)
cv2.imshow("Resized to 1/4 Size", resized_img)

# Convert grayscale back to BGR for consistent display
gray_bgr = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
cv2.imshow("Grayscale (COLOR_BGR2GRAY)", gray_bgr)
cv2.imshow("HSV Color Space (COLOR_BGR2HSV)", hsv_img)
cv2.imshow("LAB Color Space (COLOR_BGR2LAB)", lab_img)
cv2.imshow("YCrCb Color Space (COLOR_BGR2YCrCb)", ycrcb_img)

print("\nPress any key to close all windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()
