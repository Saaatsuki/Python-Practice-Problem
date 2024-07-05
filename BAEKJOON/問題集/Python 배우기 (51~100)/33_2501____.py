def common_divisors(num1):
    divisors = []
    # 1からnum1までの範囲で、num1の約数を見つける
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            divisors.append(i)
    
    return divisors

def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# 入力からnum1とnum2を取得
num1, num2 = map(int, input().split())

# num1とnum2の最大公約数を求め、その公約数のリストを取得
divisors = common_divisors(num1, num2)

# K番目の約数が存在する場合、その約数を出力
if len(divisors) >= num2:
    print(divisors[num2 - 1])
else:
    print(0)