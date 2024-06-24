import random

pc_num_list = []
while len(set(pc_num_list))<3:
    pc_num = random.randint(0,9)
    pc_num_list.append(pc_num)
pc_num_list_sum = (list(set(pc_num_list)))
print(pc_num_list_sum)

strike = 0
ball = 0
out = 0
game_count = 0

while game_count<5 and out<3 and strike<3:
    game_count += 1
    user_num1,user_num2,user_num3 = map(int,input(f"시도 {game_count} : 입력한 숫자 : ").split())
    user_num_list = [user_num1,user_num2,user_num3]
    strike = 0
    ball = 0
    for i in range(3):
        if pc_num_list_sum[i]==user_num_list[i]:
            strike += 1
        elif user_num_list[i] in pc_num_list_sum:
            ball += 1
    if strike==0 and ball==0:
        out += 1
    out_msg = f", {out} Out" if out != 0 else ""
    print(f"결과 : {strike} Strike , {ball} Ball {out_msg}")
    

msg_result = "승리" if strike==3 else f"패배 (시도 횟수 {game_count}회 초과)" if game_count==5 else f"패배 (out 횟수 {out}회)"
print(f"게임 종료 : {msg_result}\n정답 : {' '.join(map(str, pc_num_list_sum))}")