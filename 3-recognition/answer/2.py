#!/usr/bin/env python

# 画像を読み込んでPNGで保存
# 使い方: python 2.py 変換したい画像 変換後の画像名.png

import os
import sys
import cv2

# コマンド引数の数を確認
if len(sys.argv) == 3:
    # 入力ファイルの存在を確認
    if os.path.exists(sys.argv[1]):
        # 入力ファイルを読み込み
        src = cv2.imread(sys.argv[1])
        # 入力ファイルを指定形式で保存
        cv2.imwrite(sys.argv[2], src)
    # ファイルが存在しない場合は終了
    else:
        print('File not found:', sys.argv[1])
# コマンド引数が足りない場合は終了
else:
    print('arguments: source_filename save_filename')
    sys.exit(-1)
