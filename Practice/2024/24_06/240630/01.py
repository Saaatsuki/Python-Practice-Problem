# 3개의 주사위 눈을 입력받음
a, b, c = map(int, input().split())

if a == b == c:  # 3개가 같을 경우
    print(10000 + a * 1000)
elif a == b or b == c or a == c:  # 2개가 같을 경우
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + a * 100)
else:  # 모두 다른 경우
    print(max(a, b, c) * 100)
