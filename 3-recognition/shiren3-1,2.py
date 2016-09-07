# -*- coding: utf-8 -*-
import numpy as np
import cv2

#画像の読み込み
rem = cv2.imread('rem1.jpg')

#グレースケール
gray = cv2.cvtColor(rem, cv2.COLOR_BGR2GRAY)

#ガウシアンフィルタ
gausBl = cv2.GaussianBlur(rem, (5, 5), 0)

#キャニー法
canny = cv2.Canny(rem, 50, 150)

#画像表示
cv2.imshow('元画像', rem)
cv2.imshow('グレースケール', gray)
cv2.imshow('ガウシアンフィルタによる平滑化', gausBl)
cv2.imshow('Canny法によるエッジ抽出', canny)

#画像保存
cv2.imwrite('remrem.png', rem)

cv2.waitKey(0)
cv2.destroyAllWindows()
