#Numpyを用いてx+y*zを計算するプログラム
# -*- coding: utf-8 -*-

import numpy as np

x = np.array([[2.0, 4.2],
             [3.3, 5.7]])
y = np.array([[3.5, 0.9],
             [7.2, 1.2]])
z = np.array([[1.0, 0.0],
             [0.0, 1.0]])

print(x + y.dot(z))
