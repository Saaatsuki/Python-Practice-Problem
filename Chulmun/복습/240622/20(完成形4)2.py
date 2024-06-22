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
            gugu = input("出力したい九九の段を入力してください\n")
            if "~" in gugu:
                start, end = map(int, gugu.split("~"))
                gugu_li = list(range(start, end + 1))
            else:
                gugu_li = list(map(int, gugu.split(",")))
            if guguCheck(gugu_li):
                guguCal(gugu_li)
                break
            else:
                print("2~9の数字を入力してください")

    elif menu == 2:
        while True:
            high = int(input("何段ピラミットにしますか\n"))
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
                print("2または3の数字を入力してください")

    elif menu == 3:
        print("プログラムを終了します")
        break

    else:
        print("1~3のメニューから選択してください")
