while True:
    numberA = int(input("A의 값을 입력 해주세요\n"))
    numberB = int(input("B의 값을 입력 해주세요\n"))
    if (0 > numberA or 0 > numberB):
        print("0이상 의 정수를 입력 해주세요")
        continue
    else:
        if (numberA >= numberB):
            print(numberA - numberB)
            break
        else:
            print(numberB - numberA)
            break