numberA = int(input("첫 번째 숫자(정수)를 입력하세요 : "))
numberB = float(input("두 번째 숫자(부동 소수점 수)를 입력하세요 : "))

result = numberA + numberB

if (result >= 100):
    print("합이 100 이하압니다 : ", result)
else:
    print("합이 100을 초과합니다 : ", result)