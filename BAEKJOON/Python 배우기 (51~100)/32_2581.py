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

num1 = int(input())
num2 = int(input())

li = []
for i in range(num1 , num2+1):
    if is_prime(i):
        li.append(i)

print(f"{sum(li)}\n{min(li)}") if len(li)>0 else print(-1)