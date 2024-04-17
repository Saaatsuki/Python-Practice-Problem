# 入力を受け取る
n = int(input())

# 和を初期化
total = 0
# 加算した整数の個数を初期化
count = 0

# 1から順に加算し続ける
while total < n:  # 和が入力された整数よりも大きくなるまでループ
    count = count + 1  # 加算した整数の個数を1つ増やす
    total = total + count  # 加算した整数を和に加える

# 最後に加算した整数を出力
print(count)