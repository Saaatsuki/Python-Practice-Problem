def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        return f"{n} = " + " + ".join(map(str, divisors))
    else:
        return f"{n} is NOT perfect."

while True:
    n = int(input())
    if n == -1:
        break
    print(is_perfect_number(n))
