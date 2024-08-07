# ユークリッドの互除法を使って最大公約数を求める関数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 最小公倍数を求める関数
def lcm(a, b):
    return a * b // gcd(a, b)


T = int(input())

for _ in range(T):
    num1,num2 = map(int,input().split())
    print(lcm(num1,num2))
