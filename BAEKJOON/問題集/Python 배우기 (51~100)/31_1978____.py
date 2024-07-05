def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def find_primes(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# 入力から数の数 N を取得
N = int(input())

# N個の数をリストとして入力し、空白で分割して整数リストに変換
numbers = list(map(int, input().split()))

# 素数を見つけて出力
prime_numbers = find_primes(numbers)
print(len(prime_numbers))
