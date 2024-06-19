import random

def getGuguCheck(argList):
    for i in range(len(argList)):
        if 2<=argList[i]<=9:
            return True
        else:
            return False

def getGuguCal(argList):
    if len(argList)==1:
        for i in range(1,10):
            print(f"{argList[0]} X {i} = {argList[0]*i}")
    else:
        for i in range(argList[0],argList[1]+1):
            print()
            for j in range(1,10):
                print(f"{i} X {j} = {i*j}")

def getTriMake(argNum):
    com_num_li = getTriRandom(argNum)
    index = 0
    for i in range(1, argNum + 1):
        num_str = "".join(map(str, com_num_li[index:index + i]))
        print(f"{' ' * (argNum - i)}{num_str}")
        index += i

def getTriRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1, 10), num_k)


print("-"*20)
print("1) 九九の段　出力")
print("2) ランダム三角形　出力")
print("3) 終了")
print("-"*20)

while True:
    menu_num = int(input("メニューを選択してください　："))
    if menu_num == 1:
        while True:
            user_num_str = list(input("出力したい九九の段を入力してください（例：2,2~5）\n"))
            if "~" in user_num_str:
                user_num_str.remove("~")
            user_num_int = [int(i) for i in user_num_str]# list(map(int,user_num_str))
            if not getGuguCheck(user_num_int):
                print("2~9の値を入力してください")
            else :
                break
        getGuguCal(user_num_int)

    elif menu_num == 2:
        while True:
            user_num = int(input("三角形の高さを入力してください（２以上３以下）："))
            if user_num in [2, 3]:
                getTriMake(user_num)
                break
            else:
                print("2もしくは3を入力してください")

    elif menu_num == 3:
        print("プログラム終了")
        break
    else:
        print("1から3の間の数字を入力してください")    