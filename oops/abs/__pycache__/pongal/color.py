import cv2

# 1. Load the image
img = cv2.imread(r"C:\Users\saian\OneDrive\Desktop\dsp ay25-26\oops\abs\__pycache__\pongal\image.jpg")

if img is not None:
    # 2. Pick one pixel (for example: the top-left pixel at 0,0)
    # OpenCV uses BGR format
    pixel = img[0, 0] 
    blue, green, red = pixel

    print(f"--- Color Values for Pixel at (0,0) ---")
    
    # 3. Show Decimal values (0-255)
    print(f"Decimal: Blue={blue}, Green={green}, Red={red}")

    # 4. Show Binary values (8-bit)
    print(f"Binary:  Blue={blue:08b}, Green={green:08b}, Red={red:08b}")

else:
    print("Image not found!")