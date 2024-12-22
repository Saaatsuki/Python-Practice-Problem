# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 메인 함수
def main():
    # M과 N 입력
    M = int(input())
    N = int(input())
    
    primes = []
    
    # M이상 N이하의 수 중 소수 찾기
    for num in range(M, N + 1):
        if is_prime(num):
            primes.append(num)
    
    if primes:
        print(sum(primes))  # 소수들의 합 출력
        print(min(primes))  # 소수 중 최솟값 출력
    else:
        print(-1)  # 소수가 없으면 -1 출력

# 함수 호출
if __name__ == "__main__":
    main()
