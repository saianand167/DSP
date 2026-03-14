import cv2
import numpy as np
img = cv2.imread(r"C:\Users\saian\OneDrive\Desktop\dsp ay25-26\oops\abs\__pycache__\pongal\image.jpg")
if img is not None:
    matrix = np.array(img)
    print("Matrix created successfully!")
    print(matrix)
else:
    print("Error: Image not found. Please check if 'image.jpg' is in that folder.")
