import random
# 구구단 숫자 확인 함수
def true_num(num):
    if len(num) > 2:
        for i in num:
            if i == "~":
                num_a, num_b = map(int,num.replace("~"," ").split())
                if 2 <= int(num_a) <= 9 and 2 <= int(num_b) <= 9:
                    gugudan(num_a, num_b)
                else:
                    return False
    else:
        if 2 <= int(num) <= 9:
            gugudan(num)
        else:
            return False

# 메뉴 1의 구구단 계산 함수
def gugudan(num1, num2=None):
    if num2 == None:
        for i in range(1, 10):
            print(f"{num1} * {i} = {num1 * i}")
    else:
        for dan in range(num1, num2 + 1):
            print()
            for i in range(1, 10):
                print(f"{dan} * {i} = {dan * i}")

# 메뉴 2의 랜덤값 삼각형 출력 
def randomTriangle(height):
    for h in range(height):
        num_li = []
        for _ in range(height - (h+1)):
            num_li.append(" ")  
        while len(num_li) == height:
            random_num = random.randint(0,9)
            flag = True
            for i in num_li:
                if i == random_num:
                    flag = False
            if flag:
                num_li.append(random_num)
        print(*num_li)


# 메뉴출력
while True:
    print("-" * 20)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-" * 20)

    # 1, 2, 3 입력 받기
    input_menu = int(input("원하는 메뉴 번호를 입력하세요: "))

    # 1. 구구단 2~9
    if input_menu == 1:
        while True:
            print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
            input_num = input()
            flag = true_num(input_num)
            if flag:
                break
            else:
                print("2~9 사이의 값으로 입력하세요")

    # 2. 랜덤 삼각형
    elif input_menu == 2:
        while True:
            print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
            value = int(input())
            if value == 2 or value == 3:
                randomTriangle(value)
                break
            else:
                print("2 또는 3을 입력하세요")

    # 3. 종료
    elif input_menu == 3:
        print("프로그램을 종료합니다.")
        break

    # 예외처리
    else:
        print("1~3의 값을 입력하세요")