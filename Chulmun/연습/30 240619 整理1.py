import random

def gugudan():
    while True:
        user_input = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n")
        user_input_list = [int(num) for num in user_input.split("~")]

        if len(user_input_list) == 1:
            num = user_input_list[0]
            if 2 <= num <= 9:
                for i in range(1, 10):
                    print(f"{num} * {i} = {num * i}")
                break
            else:
                print("2~9 사이의 값으로 입력하세요")

        elif len(user_input_list) == 2:
            start, end = user_input_list
            if 2 <= start <= 9 and 2 <= end <= 9 and start <= end:
                for num in range(start, end + 1):
                    for i in range(1, 10):
                        print(f"{num} * {i} = {num * i}")
                    print("")
                break
            else:
                print("2~9 사이의 값으로 입력하세요")
        else:
            print("잘못된 형식입니다. 다시 입력하세요.")

def triangle():
    while True:
        height = int(input("삼각형의 높이 줄 수를 입력하세요 (2 또는 3): "))
        if height == 2 or height == 3:
            break
        else:
            print("2 또는 3을 입력하세요")

    if height == 2:
        triangle_data = [random.randint(1, 9) for _ in range(3)]
        for i in range(2):
            print(f" {' ' * (2 - i)}{triangle_data[i]}")

    elif height == 3:
        triangle_data = [random.randint(1, 9) for _ in range(6)]
        index = 0
        for i in range(3):
            print(f" {' ' * (2 - i)}", end="")
            for j in range(i + 1):
                print(triangle_data[index], end="")
                index += 1
            print()

while True:
    print("-"*20)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-"*20)
    user_menu_input = int(input("원하는 메뉴 번호를 입력하세요: "))
    if user_menu_input == 1:
        gugudan()
    elif user_menu_input == 2:
        triangle()
    elif user_menu_input == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 사이의 값을 입력하세요")
