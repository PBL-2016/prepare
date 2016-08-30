
# クイックソート

def quicksort(alist):
    # リストの要素が空ならそれを返す
    if len(alist) < 1:
        return alist

    # 左端の値をピボットに設定(中心)
    pivot = alist[0]

    # ピボット以下の値のリスト(左側)
    left = []

    # ピボットより大きい値のリスト(右側)
    right = []

    # ピボットの値とリストのそれぞれの値を比較して、不等号に応じて振り分ける
    for i in range(1, len(alist)):
        # リストの要素がピボット以下の場合はleftに入れる
        if alist[i] <= pivot:
            left.append(alist[i])
        # リストの要素がピボットより大きい場合はrightに入れる
        else:
            right.append(alist[i])

    # 左側と右側に再帰的にアルゴリズム適用
    left = quicksort(left)
    right = quicksort(right)

    # 完全にソートされたリストを結合して返す
    return left + [pivot] + right

# リストを作成
lst = [1, 14, 51, 4, 1, 9, 19, 8, 10, 8, 9, 3]

# ソート前のリストを出力
print("ソート前:", str(lst))

# リストにクイックソートを適用
lst = quicksort(lst)

# ソート後のリストを出力
print("ソート後:", str(lst))
