def prime_factors(n):
    # 2로 나누어 떨어지면 계속 나누기
    while n % 2 == 0:
        print(2)
        n //= 2
    
    # 3부터 n의 제곱근까지의 홀수들로 나누어보기
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 2
    
    # 남은 n이 소수일 경우
    if n > 2:
        print(n)

# 입력 받기
N = int(input())

# N이 1인 경우에는 출력하지 않음
if N > 1:
    prime_factors(N)
