#-*- coding: utf-8 -*-

#filter2Dの手実装(ラプラシアンフィルタ)

import numpy as np
import cv2

kernel = np.array([
    [ 0,  0, -1,  0,  0],
    [ 0, -1, -2, -1,  0],
    [-1, -2, 17, -2, -1],
    [ 0, -1, -2, -1,  0],
    [ 0,  0, -1,  0,  0]], np.float32)

if __name__ == '__main__':
    img = cv2.imread('lenna.jpg')

    kernel_h, kernel_w = kernel.shape
    img_h, img_w, depth = img.shape
    result = np.zeros((img_h, img_w, depth))

    for y in range(img_h - 1):  #画像データの高さ分繰り返し
        for x in range(img_w - 1):  #画像データの幅分繰り返し

            if(y < 2)or(x < 2)or((img_h)-2 < y)or((img_w)-2 < x):  #端の処理
                result[y][x] = img[y][x]

            else:  #値の計算
                tmp = []  #仮の値置き場

                for i in range(kernel_h - 1):  #カーネルの高さ分繰り返し
                    for j in range(kernel_w - 1):  #カーネルの幅分繰り返し
                        tmp.append(img[y-2+i][x-2+j]*kernel[i][j])
                        
                result[y][x] = sum(tmp)

    cv2.imshow('befer', img)
    cv2.imshow('after', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

