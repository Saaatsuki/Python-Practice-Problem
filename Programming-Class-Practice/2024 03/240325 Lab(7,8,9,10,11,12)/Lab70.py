# 사용자로부터 첫 번째 숫자를 입력받습니다.
num1 = int(input("첫 번째 숫자를 입력해주세요 : "))
# 사용자로부터 두 번째 숫자를 입력받습니다.
num2 = int(input("두 번째 숫자를 입력해주세요 : "))


# 입력받은 두 숫자를 더하여 결과를 저장합니다.
addition = num1 + num2
# 입력받은 두 숫자를 빼서 결과를 저장합니다.
subtraction = num1 - num2
# 입력받은 두 숫자를 곱하여 결과를 저장합니다.
multiplication = num1 * num2
# 입력받은 첫 번째 숫자를 두 번째 숫자로 나누어 결과를 저장합니다.
division = num1 / num2


# addition,subtraction,multiplication,division 결과를 출력합니다.
print("합:",addition)
print("차:",subtraction)
print("곱:",multiplication)
print("나눗셈:",division)