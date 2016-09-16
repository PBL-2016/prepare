
# OpenCVで平滑化フィルタリング

import cv2
import numpy as np

cv2.namedWindow('before')
cv2.namedWindow('after')

img = cv2.imread('lenna.png')

cv2.imshow('before', img)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('after', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
