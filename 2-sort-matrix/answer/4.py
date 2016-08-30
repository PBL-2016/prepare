
# x + y * z を計算

import numpy as np

# それぞれの行列を作成
x = np.array([[2.0, 4.2], [3.3, 5.7]])
y = np.array([[3.5, 0.9], [7.2, 1.2]])
z = np.eye(2)

# それぞれの行列を出力
print("x=")
print(x, end="\n\n")

print("y=")
print(y, end="\n\n")

print("z=")
print(z, end="\n\n")

# x + y * z を計算
# ただし普通にy*zとするとアダマール積になってしまうため、
# ドット積専用のメソッド(np.dot)を利用する
result = x + np.dot(y, z)

# 計算結果を出力
print("x + y * z =")
print(result)
