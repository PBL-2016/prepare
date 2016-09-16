
# フィルタリングを手実装

import cv2
import numpy as np


def convolution(data, kernel):
    kh, kw = kernel.shape
    if (kw % 2) != 0 | (kh % 2) != 0:
        print("カーネルの行数/列数は奇数にしてください")
        return
    cx = kw // 2
    cy = kh // 2

    dh, dw, depth = data.shape
    result = np.zeros((dh, dw, depth))
    for y in range(dh):
        for x in range(dw):
            if x < cx or y < cy or dw-x-1 < cx or dh-y-1 < cy:
                result[y][x] = data[y][x]
            else:
                t = []
                for i in range(kh):
                    for j in range(kw):
                        t.append(data[y-cy+i][x-cx+j]*kernel[i][j])
                result[y][x] = sum(t)
    return result

# kernel = np.ones((5, 5), np.float32) / 25

# 水平輪郭抽出カーネル
kernel = np.array([
    [0, 0, 0, 0, 0],
    [0,-1,-2,-1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0]], np.float32) / 16

img = cv2.imread('lenna.png')

print("処理にしばらく時間がかかります……")
dst = convolution(img, kernel).astype(np.uint8)
print("変換完了！")

cv2.namedWindow('before')
cv2.namedWindow('after')

cv2.imshow('before', img)
cv2.imshow('after', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
