# T = int(input())

# num_sum = 1
# for _ in range(T):
#     num = int(input())
#     num_sum += num

# print(num_sum - T)

import sys

# 入力を一度に読み込む
input = sys.stdin.read

# 全ての入力をリストに格納
data = input().split()

# 最初の値はマルチタップの数T
T = int(data[0])

# コンセントの数を全て合計
num_sum = 0
for i in range(1, T + 1):
    num_sum += int(data[i])

# 結果を出力
# 合計から (T-1) を引くのは、接続に1つずつ使われるから
print(num_sum - (T - 1))
