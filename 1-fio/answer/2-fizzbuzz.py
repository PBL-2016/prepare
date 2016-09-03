
# FizzBuzzの結果をファイルに出力

# 出力用のファイルを書き込みモードで開く。
f = open('fb.result', 'w')

# 1から30までFizzBuzz判定してファイルに書き込む
for i in range(1,31):
    if i % 15 == 0:
        f.write('FizzBuzz')
    elif i % 5 == 0:
        f.write('Buzz')
    elif i % 3 == 0:
        f.write('Fizz')
    else:
        f.write(str(i))
    # 改行処理
    f.write('\n')

f.close()
