
# sample.txtの数学の得点の平均値をoutput.datに出力する

# ../sample.txtを読み込みモードで開く
sample = open('../sample.dat', 'r')
# output.datを書き込みモードで開く
output = open('output.dat', 'w')

# 各列のラベルを配列に格納
labels = sample.readline().split(', ')
# readline()でsampleから1行読み出して
# split(', ')で行の内容を区切っている

# 数学のラベルの位置を検索
midx = labels.index('数学')

# 合計値蓄積用変数
total = 0

# 行の数をカウントするための変数
data_num = 0

# データ行から数学の値を取り出してtotalに加算
for line in sample:
    points = line.split(',')
    data_num += 1
    total += int(points[midx])

# 平均値を出力
output.write(str(total/data_num))

sample.close()
output.close()
