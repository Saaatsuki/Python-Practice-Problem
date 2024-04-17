# 整数を入力
n = int(input())

# 偶数の和を格納する変数を初期化
even_sum = 0

# 1からnまでの数に対してループを実行
for i in range(1, n+1):
    # 数が偶数である場合
    if i % 2 == 0:
        # 偶数の和に加算
        even_sum += i

# 偶数の和を出力
print(even_sum)
