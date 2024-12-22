def find_divisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

while True:
    n = int(input())  # 입력을 받음
    if n == -1:
        break  # 입력이 -1이면 종료
    
    divisors = find_divisors(n)
    if sum(divisors) == n:  # 완전수인지 확인
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
