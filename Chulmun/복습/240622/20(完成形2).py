import random

def guguCheck(argList):
    return all(2<=num<=9 for num in argList)

def guguCal(argList):
    for num1 in argList:
        print()
        for num2 in range(1,10):
            print(f"{num1} X {num2} = {num1*num2}")

def piramittoRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1,9),num_k)


print("-"*20)
print("1）九九の計算")
print("2）数字ピラミット")
print("3）プログラム終了")
print("-"*20)

while True:
    menu = int(input("メニュー番号を選んでください："))


# 九九の段プログラム
    if menu == 1:
        while True:
            gugu_str = input("出力する九九の段を入力してください（例：2,2~9）\n")
            if "~" in gugu_str:
                start, end = map(int, gugu_str.split("~"))
                gugu_num_li = list(range(start, end + 1))
            else:
                gugu_num_li = list(map(int, gugu_str.split(",")))

            if guguCheck(gugu_num_li):
                guguCal(gugu_num_li)
                break
            else:
                print("2~9の数字を入力してください。")


# 数字ピラミットのプログラム
    elif menu == 2:
        while True:
            high = int(input("何段ピラミットにしますか："))
            if high == 2 or high == 3:
                index = 0
                ran_li_1 = piramittoRandom(high)
                for i in range(1, high + 1):
                    ran_li_2 = ran_li_1[index:index+i]
                    ran_li_output = "".join(f"{num}" for num in ran_li_2)
                    print(f"{' ' * (high - i)}{ran_li_output}")
                    index += i
                break
            else:
                print("2または3を入力してください")
    elif menu == 3:
        print("プログラム終了")
        break

    else:
        print("1~3からメニュー番号を入力してください")    