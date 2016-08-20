
# Dappunの結果をファイルに出力

f = open('dappun.result', 'w')

for i in range(1, 31):
    if i >= 20:
        f.write('！')
    elif i % 2 == 0:
        f.write('ﾘ')
    elif i > 8:
        f.write('ｭ')
    else:
        f.write('ﾌﾞ')

f.close()
