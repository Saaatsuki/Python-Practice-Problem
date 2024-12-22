while True:
    a, b = map(int, input().split())  # 두 수 입력 받기
    if a == 0 and b == 0:
        break  # 0 0이 입력되면 종료
    if b % a == 0:
        print("factor")  # a가 b의 약수
    elif a % b == 0:
        print("multiple")  # b가 a의 약수
    else:
        print("neither")  # 약수도 배수도 아님
