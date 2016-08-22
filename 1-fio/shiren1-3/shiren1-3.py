#sample.datを読み込んでoutput.datに書き込むプログラム

if __name__ == "__main__":

    a = 0          #カウンタ
    counter = 0.0    #平均を求めるのに用いるカウンタ
    math = 0.0       #数学用変数
    f = open("sample.dat", "r")  #読み込むファイルを開く
    i = open("output.dat", "w")  #書き込むファイルを開く

    line = f.readline()  #1行ずつ読み込む

    while line:  #1行ずつ処理していく
        i.write(line)
        if a > 0:    #2ライン以降
            hoge = line
            hoge = hoge[4:7]   #数学の値
            math += int(hoge)  #数学の値を足していく
            counter += 1.0
        line = f.readline()
        a += 1
    
    math = math/counter  #数学の平均値計算

    i.write("\n\n数学の得点の平均値：")
    i.write(str(math))

    f.close()
    i.close()
