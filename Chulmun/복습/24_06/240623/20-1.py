import random

def guguCal(argList):
    for num1 in argList:
        print()
        for num2 in range(1, 10):
            print(f"{num1} X {num2} = {(num1 * num2):02d}")

def pirRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1, 10), num_k)

while True:
    print("-" * 20)
    print("1）九九の段プログラム")
    print("2）数字ピラミッド")
    print("3）終了")
    print("-" * 20)

    try:
        menu = int(input("メニュー番号を選択してちゃむ💛："))

        if menu == 1:
            while True:
                gugu = input("出力したい九九の段を入力してちゃむ💛（例：2,2~5）:")
                if "~" in gugu:
                    start, end = map(int, gugu.split("~"))
                    gugu_li = list(range(start, end + 1))
                else:
                    gugu_li = list(map(int, gugu.split(",")))
                if all(2 <= num <= 9 for num in gugu_li):
                    guguCal(gugu_li)
                    break
                else:
                    print("2~9の数字を入力してちゃむ💙")

        elif menu == 2:
            while True:
                high = int(input("何段の数字ピラミッドにするちゃむ？💛："))
                if high == 2 or high == 3:
                    li1 = pirRandom(high)
                    index = 0
                    for i in range(1, high + 1):
                        li2 = li1[index:index + i]
                        li3 = "".join(f"{num}" for num in li2)
                        print(f"{' ' * (high - i)}{li3}")
                        index += i
                    break
                else:
                    print("2~3の数字を入力するちゃむ💙")

        elif menu == 3:
            print("プログラムを終了するちゃむ💛")
            break

        else:
            print("1～3からメニュー番号を選ぶちゃむ💙")

    except ValueError:
        print("有効な数値を入力してちゃむ💙")
