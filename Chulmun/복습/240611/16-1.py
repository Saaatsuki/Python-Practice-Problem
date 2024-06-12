import random

com_num_ind_set = set()
while len(com_num_ind_set) < 3:
    com_num_ind = random.randint(0, 9)
    com_num_ind_set.add(com_num_ind)
com_num_ind_li = list(com_num_ind_set)
game_count = 0
strike = 0
ball = 0
out = 0
while game_count < 5 and strike < 3 and out < 3:
    game_count += 1
    num1, num2, num3 = map(int, input(f"시도 {game_count} : 입력한 숫자 - ").split())
    user_num_li = [num1, num2, num3]
    strike = 0
    ball = 0

    for i in range(3):
        if user_num_li[i] == com_num_ind_li[i]:
            strike += 1
        elif [num for num in com_num_ind_li if num == user_num_li[i]]:
            ball += 1
    msg_strike = f"{strike} Strike"
    msg_ball = f"{ball} Ball"
    msg_out = ""
    if strike == 0 and ball == 0:
        out += 1
        msg_out = f", {out} Out"
    print(f"결과 : {msg_strike}, {msg_ball}{msg_out}")

msg_res = "승리" if strike == 3 else f"패배(시도 횟수 {game_count}회 초과)" if game_count == 5 else "패배"
print(f"게임 종료 : {msg_res}\n정답 : {' '.join(map(str, com_num_ind_li))}")