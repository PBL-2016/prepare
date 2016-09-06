# -*- coding: utf-8 -*-
import numpy as np
import cv2

#画像の読み込み
rem = cv2.imread('rem2.png')

#グレースケール化
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ガウシアンフィルタ
#gaussianBlured = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow('remrin', rem)
cv2.waitKey(0)
cv2.destroyAllWindows()
