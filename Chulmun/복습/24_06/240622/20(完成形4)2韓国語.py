import random

def guguCheck(argList):
    return all(2 <= num <= 9 for num in argList)

def guguCal(argList):
    for num1 in argList:
        print()
        for num2 in range(1, 10):
            print(f"{num1} X {num2} = {(num1 * num2):02d}")

def piramittoRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1, 10), num_k)

while True:
    print("-" * 20)
    print("1）구구단 출력")
    print("2）랜덤값 삼각형 출력")
    print("3）프로그램 종료")
    print("-" * 20)

    menu = int(input("원하는 메뉴 번호를 입력하세요 : "))

    if menu == 1:
        while True:
            gugu = input("출력하고 싶은 구구단 단수를 입력하세요\n")
            if "~" in gugu:
                start, end = map(int, gugu.split("~"))
                gugu_li = list(range(start, end + 1))
            else:
                gugu_li = list(map(int, gugu.split(",")))
            if guguCheck(gugu_li):
                guguCal(gugu_li)
                break
            else:
                print("2~9 사이의 숫자를 입력하세요")

    elif menu == 2:
        while True:
            high = int(input("몇 단 삼각형을 만드시겠습니까?\n"))
            if high == 2 or high == 3:
                li1 = piramittoRandom(high)
                index = 0
                for i in range(1, high + 1):
                    li2 = li1[index:index + i]
                    li3 = "".join(f"{num:02d}" for num in li2)
                    print(f"{' ' * (high - i)}{li3}")
                    index += i
                break
            else:
                print("2 또는 3을 입력하세요")

    elif menu == 3:
        print("프로그램을 종료합니다")
        break

    else:
        print("1~3 사이의 메뉴 번호를 선택하세요")
