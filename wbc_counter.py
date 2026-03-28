import cv2
import numpy as np
# Read the input image (replace 'cell.png' with your actual image file)
image = cv2.imread("wbc.jpg", cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Apply Hough Circle Transform
circles = cv2.HoughCircles(
    image,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=20,
    param1=50,
    param2=28,
    minRadius=1,
    maxRadius=20,
)

# Count the detected circles (WBCs)
if circles is not None:
    WBC_count = len(circles[0])
else:
    WBC_count = 0

print(f"Number of white blood cells (WBCs): {WBC_count}")

# Display the image with detected circles
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)

    cv2.imshow("Detected WBCs", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No WBCs detected.")

