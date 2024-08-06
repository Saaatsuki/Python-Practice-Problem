num = int(input())
n = 2

while num > 1:
    if num % n == 0:
        num = num // n
        print(n)
    else:
        n += 1
