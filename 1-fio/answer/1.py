
# ファイルを開いて中身を標準出力

# file.txtを読み込みモードで開いて変数fにバインド
f = open('file.txt', 'r')

# ファイルの内容を行単位で表示
for line in f:
    print(line, end='')

# ファイルを閉じる
f.close()
