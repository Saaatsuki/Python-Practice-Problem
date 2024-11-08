import random

# 배열의 크기 N을 입력받아 유효성 검사
while True:
    try:
        N = int(input("배열의 크기 N을 입력하세요: "))
        if N > 0:
            break
        else:
            print("N은 0보다 커야 합니다. 다시 입력하세요.")
    except ValueError:
        print("정수를 입력하세요.")

# 난수 범위를 지정할 start, end 값을 입력받아 유효성 검사
while True:
    try:
        start = int(input("난수 범위의 시작값 start를 입력하세요: "))
        end = int(input("난수 범위의 끝값 end를 입력하세요: "))
        if end >= start and (end - start + 1) >= N:
            break
        else:
            print(f"범위 크기 ({end - start + 1})는 배열 크기 N({N})보다 커야 합니다. 다시 입력하세요.")
    except ValueError:
        print("정수를 입력하세요.")

# 배열 생성 및 난수 채우기
array = [random.randint(start, end) for _ in range(N)]

# 배열 출력
print("생성된 배열:", array)