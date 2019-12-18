import cv2
import numpy as np
Th = 0.3
Tl = 0.1
img = cv2.imread("src/img.jpg")
min = Tl*np.max(np.array(img))
max = Th*np.max(np.array(img))
edges = cv2.Canny(img, min, max)
cv2.imwrite('result2/cv2.jpg', edges)