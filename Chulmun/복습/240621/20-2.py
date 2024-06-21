import random

def guguCheck(guguList):
    return all(2 <= x <= 9 for x in guguList)

def guguCal(argList):
    if len(argList) == 1:
        for i in range(2, 10):
            print(f"{argList[0]} X {i} = {argList[0] * i}")
    else:
        for i in range(argList[0], argList[1] + 1):
            print()
            for j in range(2, 10):
                print(f"{i} X {j} = {i * j}")

def getTri(argNum):
    tri_li = triRandom(argNum)
    index = 0
    for i in range(1, argNum + 1):
        num_str = " ".join(map(str, tri_li[index:index + i]))
        print(f"{' ' * (argNum - i)}{num_str}")
        index += i

def triRandom(argNum):
    num_k = argNum * (argNum + 1) // 2
    return random.sample(range(1, num_k + 1), num_k)

print("-" * 20)
print("1. 구구단 출력")
print("2. 랜덤값 삼각형 출력")
print("3. 종료")
print("-" * 20)

while True:
    menu = int(input("메뉴 번호를 입력하세요:"))

    if menu == 1:
        while True:
            gugu_input = input("출력할 구구단을 아래 형식으로 입력하세요(예 : 2 , 2~5)\n")
            if "~" in gugu_input:
                gugu = list(map(int, gugu_input.split("~")))
            else:
                gugu = [int(gugu_input)]
            if not guguCheck(gugu):
                print("2~9 사이의 값을 입력하세요")
            else:
                guguCal(gugu)
                break

    elif menu == 2:
        while True:
            tri = int(input("삼각형의 높이 줄 수를 입력하세요\n"))
            if tri < 2:
                print("2 이상의 값을 입력하세요.")
            else:
                getTri(tri)
                break
    elif menu == 3:
        print("종료")
        break
    else:
        print("1~3 사이로 입력하세요.")
