# -*- coding: utf-8 -*-
# OpenCVで顔認識

import os
import sys
import cv2

# 分類器パス
CLASSIFIER_PATH = '../haarcascade_frontalface_default.xml'

# コマンド引数の数を確認
if len(sys.argv) == 2:
    # 入力ファイルの存在と、パスがファイルであることを確認
    if os.path.exists(sys.argv[1]) & os.path.isfile(sys.argv[1]):
        # 入力ファイル名(拡張子抜き)を抜き出し
        root, _ = os.path.splitext(sys.argv[1])
        # 出力ディレクトリを作成
        os.mkdir(root)

        # 分類器を読み込み
        classifier = cv2.CascadeClassifier(CLASSIFIER_PATH)

        # 入力ファイルを読み込み
        img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
        # 入力ファイルをグレースケールに変換
        gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 入力を分類器にかける
        # 引数: 入力画像, 各画像スケールにおける縮小量, 最低近傍矩形数
        face = classifier.detectMultiScale(gImg, 1.1, 3)

        # 認識した顔の矩形ごとに処理
        for i in range(len(face)):
            x = face[i][0]
            y = face[i][1]
            w = face[i][2]
            h = face[i][3]
            # 入力ファイルから顔を切り出して保存
            cv2.imwrite(root+'/'+str(i)+'.png', img[y:y+h, x:x+w])   
 # 入力ファイルが存在しない場合は終了
    else:
        print('File not found:', sys.argv[1])
        sys.exit(-1)
# コマンド引数が足りない場合は終了
else:
    print('Arguments: input_filename')
    sys.exit(-1)
