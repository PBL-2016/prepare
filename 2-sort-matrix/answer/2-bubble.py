
# バブルソート

def bubblesort(alist):
    # 値の交換が無くなるまで繰り返す
    while True:
        # 値交換チェックフラグ
        done = True
        # リストの長さ-1回繰り返す
        for i in range(len(alist)-1):
            # リストのi番目要素とi+1番目要素を比較
            if alist[i] > alist[i+1]:
                # 昇順でなかった場合は値交換
                alist[i], alist[i+1] = alist[i+1], alist[i]
                # 値交換が起こったのでフラグをFalseにする
                done = False
        # 値交換が起こっていない(done=True)場合はwhileループを抜ける
        if done:
            break
    return alist

# リストを作成
lst = [1, 14, 51, 4, 1, 9, 19, 8, 10, 8, 9, 3]

# ソート前のリストを出力
print("ソート前:", str(lst))

# リストにバブルソートを適用
lst = bubblesort(lst)

# ソート後のリストを出力
print("ソート後:", str(lst))
