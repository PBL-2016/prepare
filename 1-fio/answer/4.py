
# ouroboros.txtの中身を2倍した数の100の剰余で上書きする

# ouroboros.txtを読み書きモードで開く
f = open('ouroboros.txt', 'r+')

# 中身を数値に変換して変数に格納
before = int(f.read())

# それを2倍した数の100の剰余を変数に格納
after = (before * 2) % 100

# ファイル書き込み位置を先頭にする
f.seek(0)

# ファイルに値を書き込む
f.write(str(after))

# ファイルサイズを書き込んだ位置まで切り詰める
f.truncate()

f.close()
