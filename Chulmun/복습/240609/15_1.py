import random

user_win = 0
pc_win = 0
aiko = 0

while user_win<2 and pc_win<2 :
    janken = ["가위","바위","보"]
    user_janken = input("가위 바위 보 중 하나를 입력하세요 : ")
    while not user_janken=="가위" and not user_janken=="바위" and not user_janken=="보":
        user_janken = input("가위 바위 보 중에서 선택하세요 : ")

    pc_jenken_num = random.randint(1,2)
    pc_janken_str = janken[pc_jenken_num]

    user_janken_num = janken.index(user_janken)
    jud = pc_jenken_num - user_janken_num

    if jud==0:
        aiko = 0
        msg_result = "무승부"
    elif jud == -1 or jud == 2 :
        user_win += 1
        msg_result = "승리"
    else:
        pc_win += 1
        msg_result = "패배"
    print(f"컴퓨터 : {pc_janken_str}\n{msg_result}!! 현재 전적 : {user_win}승 {pc_win}패 {aiko}무")
msg_winner = "사용자" if user_win==2 else "컴퓨터"
print(f"최종 승자 : {msg_winner}")

