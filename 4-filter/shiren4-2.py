# -*- coding: utf-8 -*-

#1次元配列の畳み込み処理

import numpy as np

kernel = np.array([0.5, 1.0, 0.0])
value = np.array([64, 32,128, 16,  0,256,  0, 32])

if __name__ == '__main__':
    result = np.zeros(len(value))  #結果を入れる配列の初期化

    for i in range(len(value)):
        if (i == 0)or(i == len(value)-1):  #端の処理
            result[i] = value[i]
        else:  #値の計算
            x = []
            for j in range(len(kernel)):
                x.append(value[j-1+i]*kernel[j])  
            result[i] = sum(x)

    print(result)
