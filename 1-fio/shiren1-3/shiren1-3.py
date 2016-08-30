#sample.datを読み込んでoutput.datに書き込むプログラム

if __name__ == "__main__":

    a = 0          #カウンタ
    b = 0          #数学のリストナンバーを管理
    counter = 0.0    #平均を求めるのに用いるカウンタ
    math = 0.0       #数学用変数
    f = open("sample.dat", "r")  #読み込むファイルを開く
    i = open("output.dat", "w")  #書き込むファイルを開く

    line = f.readline()  #1行ずつ読み込む

    while line:  #1行ずつ処理していく
        hoge = line

        if a == 0:   #1ライン
            hoge = hoge.split(", ")   #文字列を分割
            b = hoge.index("数学")    #数学のリストナンバーを変数に代入
        else:   #2ライン以降
            hoge = hoge.split(",")
            hoge = hoge[b]     #数学の値
            math += int(hoge)  #数学の値を足していく
            counter += 1.0

        line = f.readline()
        a += 1
    
    math = math/counter  #数学の平均値計算

    i.write("数学の得点の平均値：")
    i.write(str(math))

    f.close()
    i.close()
