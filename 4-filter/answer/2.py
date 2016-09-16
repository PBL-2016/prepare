
# 一次元配列畳み込み

import numpy as np


# 畳込み関数
def convolution(data, kernel):
    # カーネルの幅を取得
    kw = kernel.shape[0]
    # カーネルの半径を計算
    cx = kw // 2

    # データの幅を取得
    dw = data.shape[0]
    # 計算結果格納用変数を初期化
    result = np.zeros((dw))

    # データの幅の数だけ繰り返す
    for x in range(dw):
        # カーネルがデータからはみ出る場合の処理
        if x < cx or dw-x-1 < cx:
            result[x] = data[x]
        else:
            # 各番地の計算結果を格納する配列
            t = []
            # カーネルを各番地に適用して一時変数に追加
            for i in range(kw):
                t.append(data[x-cx+i]*kernel[i])
            # 合計を変換後のデータとして代入
            result[x] = sum(t)
    # 変換後のデータを返す
    return result

# カーネルを作成
# 幅は奇数にすること
kernel = np.array([0.5, 1.0, 0.0])

# データを作成
# 型は何でも良いが、表示する時のフォーマットを合わせるためにfloat32にしている
data = np.array([64, 32, 128, 16, 0, 256, 0, 32], np.float32)

# データを変換
# 演算を行うと基本的にfloat32になるので、型変換したい場合はここで行う
# 例: dst = convolution(data, kernel).astype(np.int8)
dst = convolution(data, kernel)

# 結果を表示
print("畳込み前:", data)
print("畳込み後:", dst)
