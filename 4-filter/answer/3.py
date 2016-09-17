
# フィルタリングを手実装

import cv2
import numpy as np


def convolution(data, kernel):
    # カーネルの高さと幅を取得
    kh, kw = kernel.shape
    # カーネルの行数/列数が偶数かチェック
    if (kw % 2) != 0 | (kh % 2) != 0:
        print("カーネルの行数/列数は奇数にしてください")
        return

    # カーネルの半径を求める
    cx = kw // 2
    cy = kh // 2

    # データの高さ、幅、色チャンネル数を取得
    dh, dw, depth = data.shape
    # 結果格納用変数をゼロ初期化
    result = np.zeros((dh, dw, depth))

    # データの高さだけ繰り返す
    for y in range(dh):
        # データの幅だけ繰り返す
        for x in range(dw):
            # カーネルがデータからはみ出る部分の処理
            if x < cx or y < cy or dw-x-1 < cx or dh-y-1 < cy:
                # そのままコピー
                result[y][x] = data[y][x]
            else:
                t = []
                # カーネルの高さだけ繰り返す
                for i in range(kh):
                    # カーネルの幅だけ繰り返す
                    for j in range(kw):
                        # 該当番地にカーネルを適用して一時変数に追加
                        t.append(data[y-cy+i][x-cx+j]*kernel[i][j])
                # 一時変数の和を計算結果に代入
                result[y][x] = sum(t)
    # 結果を返す
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
