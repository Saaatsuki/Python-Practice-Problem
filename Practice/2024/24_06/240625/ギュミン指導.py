import random

def checkGugu(arg_list):
    for num in arg_list:
        if not (2 <= num <= 9):
            return False
    return True

def checkTri(arg_num):
    if arg_num == 2 or arg_num == 3:
        return True
    return False

def getGugu(arg_list):
    if len(arg_list) == 2:
        arg_list = [num for num in range(arg_list[0], arg_list[1] + 1)]

    for num in arg_list:
        for j in range(1, 10):
            print(f"{num} * {j} = {num * j}")
        print()

def getTri(arg_num):
    num_list = []

    while len(num_list) < 10:
        num = random.randint(0, 9)
        if num not in num_list:
            num_list.append(num)

    index = 0
    for i in range(arg_num):
        print(" " * (arg_num - i - 1), end="")
        for _ in range(i + 1):
            print(num_list[index], end="")
            index += 1
        print()


while True:
    print("-" * 20)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-" * 20)

    user_select = int(input("원하는 메뉴 번호를 입력하세요: "))

    if not (1 <= user_select <= 3):
        print("1~3 사이의 값을 입력하세요")
        continue

    if user_select == 1:
        while True:
            user_select_1 = list(map(int, input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n").split("~")))

            if checkGugu(user_select_1):
                getGugu(user_select_1)
                break
            else:
                print("2~9 사이의 값으로 입력하세요")
                continue

    elif user_select == 2:
        while True:
            user_select_2 = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)"))

            if checkTri(user_select_2):
                getTri(user_select_2)
                break
            else:
                print("2 또는 3을 입력하세요")


    else:
        print("프로그램을 종료합니다.")
        break