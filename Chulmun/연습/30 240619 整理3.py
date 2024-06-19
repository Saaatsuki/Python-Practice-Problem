import random

def getGuguAll():
    while True:
        user_num_li = list(map(int,input(f"출력할 구구단을 아래 형식으로 입력하세요(예 : 2 , 2~5)\n").split("~")))
        if guguCheck(user_num_li):
            getGuguCal(user_num_li)
            break
        else:
            print(f"2~9 사이의 값으로 입력하세요")

def guguCheck(argList):
    for i in argList:
        if not(2<=i<=9):
            return False
    return True

def getGuguCal(argList):
    if len(argList)==1:
        for i in range(1,10):
            print(f"{argList[0]} X {i} = {argList[0]*i}")
    else:
        for i in range(argList[0],argList[1]+1):
            print()
            for j in range(1,10):
                print(f"{i} X {j} = {i*j}")

def getTryAll():
    while True:
        user_num = int(input("삼각형의 높이 줄 수를 입력하세요 (2이상 3이하): "))
        if user_num in [2, 3]:
            getTryResult(user_num)
            break
        else:
            print("2 또는 3을 입력하세요")

def getTryResult(argNum):
    com_num_li = getTryRandom(argNum)
    index = 0
    for i in range(1, argNum + 1):
        number_string = ''.join(map(str, com_num_li[index:index+i]))
        print(f"{' '*(argNum-i)}{number_string}")
        index += i


def getTryRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1, 10), num_k)

print("--------------------")
print("1) 구구단 출력")
print("2) 랜덤값 삼각형 출력")
print("3) 종료")
print("--------------------")

while True:
    menu_num = int(input("원하는 메뉴 번호를 입력하세요 : "))
    if menu_num == 1:
        getGuguAll()
    elif menu_num == 2:
        getTryAll()
    elif menu_num == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 사이의 값을 입력하세요.")