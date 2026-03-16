'''Leaf Health Detection (Plant Disease Detection)

This example uses CNN with TensorFlow.

pip install tensorflow keras numpy'''


import cv2
import numpy as np

# image load
img = cv2.imread("leaf1.jpeg")

# resize
img = cv2.resize(img,(400,400))

# convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# green color range
lower_green = np.array([25,40,40])
upper_green = np.array([90,255,255])

mask = cv2.inRange(hsv, lower_green, upper_green)

green_pixels = np.sum(mask == 255)
total_pixels = mask.size

green_ratio = green_pixels / total_pixels

print("Green Ratio:", green_ratio)

if green_ratio > 0.4:
    print("Leaf is Healthy 🌿")
else:
    print("Leaf may be Diseased 🍂")

cv2.imshow("Leaf",img)
cv2.imshow("Green Mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()