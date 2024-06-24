import random

def guguCheck(argList):
    return all(2<=num<=9 for num in argList)

def guguCal(argList):
    for num1 in argList:
        print()
        for num2 in range(1,10):
            print(f"{num1} X {num2} = {(num1*num2):02d}")

def piramittoRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1,10),num_k)

while True:
    print("-"*20)
    print("1）九九の段プログラム")
    print("2）数字ピラミットプログラム")
    print("3）プログラム終了")
    print("-"*20)
    menu = int(input("メニュー番号を選択してください："))

    if menu == 1:
        while True:
            gugu = input("出力する九九の段を入力してください（例：2,2~9）\n")
            if "~" in gugu:
                start , end = map(int,gugu.split("~"))
                gugu_li = list(range(start , end+1))
            else:
                gugu_li = list(map(int,gugu.split(",")))
            
            if guguCheck(gugu_li):
                guguCal(gugu_li)
                break
            else:
                print("2~9の数字を入力してください")

    elif menu == 2:
        while True:
            high = int(input("何段のピラミットにしますか："))
            if high==2 or high==3:
                index = 0
                for i in range(1,high+1):
                    num_li_1 = piramittoRandom(high)
                    num_li_2 = num_li_1[index:index+i]
                    num_li_3 = "".join(f"{num}" for num in num_li_2)
                    print(f"{' '*(high-i)}{num_li_3}")
                    index += i
                break
            else:
                print("2または3の数字を入力してください")
    
    elif menu == 3:
        print("プログラム終了")
        break
    
    else:
        print("1～3の数字を入力してください")

