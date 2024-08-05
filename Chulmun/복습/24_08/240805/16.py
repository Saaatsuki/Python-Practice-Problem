import random

com_num_li = []
while len(com_num_li) < 3:
    com_num = random.randint(0, 9)
    if com_num not in com_num_li:
        com_num_li.append(com_num)

game_count = 0
strike = 0
ball = 0
out = 0

while strike < 3 and out < 3 and game_count < 5:
    strike = 0
    ball = 0
    
    game_count += 1
    try:
        num1, num2, num3 = map(int, input(f"시도 {game_count} : 입력한 숫자 - ").split())
        user_num_li = [num1, num2, num3]
    except ValueError:
        print("잘못된 입력입니다. 세 개의 숫자를 입력하세요.")
        continue

    for ind in range(3):
        if com_num_li[ind] == user_num_li[ind]:
            strike += 1
        elif user_num_li[ind] in com_num_li:
            ball += 1

    if strike == 0 and ball == 0:
        out += 1

    print(f"결과 : {strike} Strike, {ball} Ball, {out} Out")

msg = "패배" if game_count >= 5 or out >= 3 else "승리"
print(f"게임 종료 : {msg}")
print(f"정답 : {' '.join(map(str, com_num_li))}")
