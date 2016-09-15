# -*- coding: utf-8 -*-

#画像の平滑化を行うプログラム

import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('lenna.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #BGRからRGBへ変換
    
    kernel = np.ones((5,5), np.float32)/25  #5x5の窓のピクセルを合計して25で割る（平均値を出す）
    dst = cv2.filter2D(img, -1, kernel)

    #pyplotを用いた表示
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]),plt.yticks([])
    plt.show()
