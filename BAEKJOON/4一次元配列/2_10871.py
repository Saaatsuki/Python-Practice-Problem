# 入力を受け取る
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 数列Aの各要素について、Xより小さいかどうかをチェックしながら出力
for num in A:
    if num < X:
        print(num, end=' ')

############################################################################


# 入力を受け取る
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 結果を保存するためのリストを初期化
result = []

# 数列Aの各要素について、Xより小さいかどうかをチェック
for num in A:
    if num < X:
        result.append(num)

# 空白で区切って出力
print(' '.join(map(str, result)))

###########################################################

# 入力を受け取る
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 結果を保存するためのリストを初期化
result = []

# 数列Aの各要素について、Xより小さいかどうかをチェック
for num in A:
    if num < X:
        result.append(num)

# 空白で区切って出力
print(' '.join(map(str, result)))
