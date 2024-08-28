# 素数判定用の関数を定義
def is_prime(num):
    if num <= 1:  # 1以下の数は素数ではない
        return False
    # 2からnumの前の数までのすべての数で割り切れるかチェック
    for i in range(2, num):
        if num % i == 0:  # 割り切れる場合は素数ではない
            return False
    return True

# 入力の読み取り
N = int(input())
num_li = list(map(int, input().split()))

# 素数の個数をカウントする変数
prime_count = 0

# 各数が素数かどうかを判定し、素数ならカウントを増やす
for num in num_li:
    if is_prime(num):
        prime_count += 1

# 結果を出力
print(prime_count)
