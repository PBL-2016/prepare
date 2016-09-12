# -*- coding: utf-8 -*-

#画像からカスケード分類器を用いて顔認識を行うプログラム

import cv2

CLASSIFIER_PATH = '../haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(CLASSIFIER_PATH)

img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = faceCascade.detectMultiScale(gray, 1.1, 3)

if len(face) > 0:
    for rect in face:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness = 2)
else:
    print("no face")

cv2.imwrite('detected.jpg', img)
cv2.imshow('detected_img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
