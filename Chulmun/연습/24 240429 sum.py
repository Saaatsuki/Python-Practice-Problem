numbers_str = map(int, input("숫자들을 쉼표로 구분하여 입력하세요 : ").split(','))
numbers = list(numbers_str)
result = sum(map(int, numbers))

if result <= 100:
    print("총합이 100을 초과하지 않습니다.")
    print("입력된 모든 숫자 : ", numbers)
    print("최종 총합 : ", result)
else:
    print("총합이 100을 초과합니다.")
    print("현재까지 입력된 값들 : ", numbers)
    print("현재까지의 총합 : ", result)
