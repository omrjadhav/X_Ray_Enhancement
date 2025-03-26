import pyautogui
import cv2
import numpy as np

# Function to enhance contrast using CLAHE (for X-ray, MRI, CT images)
def enhance_medical_image(image):
    # Convert to grayscale (most medical images are grayscale)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Convert back to BGR for display consistency
    enhanced_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

    return enhanced_bgr

# Manually select the medical image area
print("Move your mouse to the top-left of the medical image and press Enter...")
input()
x1, y1 = pyautogui.position()

print("Move your mouse to the bottom-right of the medical image and press Enter...")
input()
x2, y2 = pyautogui.position()

# Calculate width and height of the selected region
capture_region = (x1, y1, x2 - x1, y2 - y1)

while True:
    # Capture medical image from the screen
    img = pyautogui.screenshot(region=capture_region)

    # Convert the screenshot to an OpenCV format
    image = np.array(img)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Enhance the captured medical image
    enhanced_image = enhance_medical_image(image)

    # Display both original and enhanced images side by side
    combined = np.hstack([image, enhanced_image])
    cv2.imshow("Medical Image Enhancement", combined)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close the OpenCV window
cv2.destroyAllWindows()
