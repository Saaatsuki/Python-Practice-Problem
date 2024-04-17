# 변의 길이를 세개 입력받습니다.
num1 = int(input("첫 번째 변의 길이를 입력해주세요："))
num2 = int(input("두 번째 변의 길이를 입력해주세요："))
num3 = int(input("세 번째 변의 길이를 입력해주세요："))

# 입력된 변의 길이로 삼각형을 만들 수 있는지 확인합니다.
msg = "입력하신 변이 길이로는 {}삼각형 만들 수 있습니다."


# 삼각형을 만들 수 있는 경우, 삼각형의 유형을 판별합니다.
if ((num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1)):
    if num1 == num2 == num3:
        print(msg.format("정"))
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print(msg.format("이등변"))
    else:
        print(msg.format("부등변"))
else: # 삼각형을 만들 수 없는 경우, 그 이유를 출력합니다.
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 나머지 한 변의 길이보다 커야 합니다.")