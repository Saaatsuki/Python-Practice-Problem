import random

com_ind_set = set()
while len(com_ind_set) < 3:
    com_ind = random.randint(0, 9)
    com_ind_set.add(com_ind)
com_ind_li = list(com_ind_set)
print(com_ind_li)

strike = 0
ball = 0
out = 0
game_count = 0

while game_count < 5 and strike < 3 and out < 3:
    game_count += 1
    strike = 0
    ball = 0
    num1, num2, num3 = map(int, input(f"시도 {game_count} : 입력한 숫자 - ").split())
    user_li = [num1, num2, num3]
    for i in range(3):
        if com_ind_li[i] == user_li[i]:
            strike += 1
        elif len([j for j in com_ind_li if j==user_li[i]])>0:#user_li[i] in com_ind_li:
            ball += 1
    out_msg = ""
    strike_msg = f"{strike} Strike!!"
    ball_msg = f"{ball} Ball!!"
    if strike == 0 and ball == 0:
        out += 1
    out_msg = "" if out == 0 else f", {out} Out!!"
    print(f"결과 : {strike_msg}, {ball_msg}{out_msg}")

msg = "승리" if strike == 3 else f"패배 (시도 횟수 {game_count}회 초과)" if game_count == 5 else f"패배"
print(f"게임 종료 : {msg}\n정답 : {' '.join(map(str, com_ind_li))}")