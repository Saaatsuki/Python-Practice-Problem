while True:
    numbers = []

    for i in range(1, 3):
        number = int(input(f"{i}번째 의 정수를 입력 해주세요 : "))
        numbers.append(number)

    if (numbers[1] == 0):
        print("0 값으로 나눌 수 없습니다.")
    elif (numbers[0] < numbers[1]):
        print("첫 번째 값보다 큰 값을 입력하세요.")
    else:
        result = numbers[0] / numbers[1]
        print("결과", result)
        break
