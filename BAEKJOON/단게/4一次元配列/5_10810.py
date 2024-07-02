# 入力の読み込み
n, m = map(int, input().split())

# バスケットの初期化
baskets = [0] * n

# 操作の処理
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):  # i-1からjまでを更新
        baskets[idx] = k

# 結果の出力
print(*baskets)

#print(" ".join(map(str,baskets)))