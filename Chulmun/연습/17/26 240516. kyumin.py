import random

def getComputerNumber():
    number_list = []

    while len(number_list) < 3:
        number = random.randint(0, 9)
        isExist = False
        for num in number_list:
            if num == number:
                isExist = True
        if not isExist:
            number_list.append(number)

    return number_list

def getStrikeAndBall(argList):
    strike = 0
    ball = 0

    for i in range(3):
        for j in range(3):
            if computer_list[i] == argList[j] and i == j:
                strike += 1
            elif computer_list[i] == argList[j]:
                ball += 1

    return strike, ball
    
    

computer_list = getComputerNumber()
win = False
strike_out = 0

for i in range(5):
    
    user_list = list(map(int, input(f"시도 {i + 1}: 입력한 숫자 - ").split()))
    strike, ball = getStrikeAndBall(user_list)
    out = 3 - strike - ball

    print(f"결과: {strike} Strike, {ball} Ball, {out} Out")
    
    if strike == 3:
        win = True
        break
    
    if strike_out == 2:
        break
    
    if out == 3:
        strike_out += 1

if win:
    print("\n게임 종료: 승리")
else:
    print("게임 종료: 패배 (시도 횟수 5회 초과)")

print(f"정답: {" ".join(map(str, computer_list))}")