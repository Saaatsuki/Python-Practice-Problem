# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2는 소수
    for i in range(2, int(num**0.5) + 1):  # i*i <= num을 최적화
        if num % i == 0:
            return False  # 나누어 떨어지면 소수가 아님
    return True

# 메인 함수
def main():
    # 수의 개수 입력
    N = int(input())
    
    count = 0
    
    # 주어진 N개의 수를 읽어서 소수인지 판별
    for _ in range(N):
        num = int(input())
        if is_prime(num):
            count += 1
    
    # 결과 출력
    print(count)

# 함수 호출
if __name__ == "__main__":
    main()
