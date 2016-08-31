
# 画像を読み込んでウィンドウに表示

import cv2

# ImgViewウィンドウ作成
cv2.namedWindow('ImgView')

# 画像を読み込む
img = cv2.imread('./Lenna.jpg')

# ImgViewに画像を表示
cv2.imshow('ImgView', img)

# キー入力があるまで待機
cv2.waitKey(0)

# 全てのウィンドウを閉じる
cv2.destroyAllWindows()
