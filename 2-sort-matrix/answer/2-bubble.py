
# バブルソート

# バブルソートの1イテレーションでリストを一巡すると
# 比較を終えた位置の大小関係が確定します。
# アルゴリズム上、未確定範囲の中で一番小さい値が左に
# 運ばれていくからです。


def bubblesort(alist):
    # リストの最後の要素の位置を格納
    last = len(alist)-1
    # 未確定範囲始点をiとする
    for i in range(len(alist)):
        # 比較位置を最後の位置に戻す
        j = last
        # 未確定範囲始点と比較位置が同じになるまで繰り返す
        while not i == j:
            # リストのj-1番目要素とj番目要素を比較
            if alist[j-1] > alist[j]:
                # 昇順でなかった場合は値交換
                alist[j-1], alist[j] = alist[j], alist[j-1]
            # 比較位置を1つ手前に移動
            j -= 1
    # ソート後のリストを返す
    return alist

# リストを作成
lst = [1, 14, 51, 4, 1, 9, 19, 8, 10, 8, 9, 3]

# ソート前のリストを出力
print("ソート前:", str(lst))

# リストにバブルソートを適用
lst = bubblesort(lst)

# ソート後のリストを出力
print("ソート後:", str(lst))
