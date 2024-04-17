# 사용자로부터 세 번째까지 숫자를 입력받습니다.
num1 = int(input("첫 번째 숫자를 입력해주세요: "))
num2 = int(input("두 번째 숫자를 입력해주세요: "))
num3 = int(input("세 번째 숫자를 입력해주세요: "))


# 입력받은 세 숫자 중에서 가장 큰 숫자를 찾습니다.
max_number = max(num1,num2,num3)

# 가장 큰 숫자를 출력합니다.
print("가장 큰 숫자는",max_number,"입니다.")