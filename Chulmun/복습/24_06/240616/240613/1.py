import random

pc_num_set = set()
while len(pc_num_set)<3:
    pc_num_ind = random.randint(0,9)
    pc_num_set.add(pc_num_ind)
pc_num_li = list(pc_num_set)
print(pc_num_li)

game_count = 0
strike = 0
ball = 0
out = 0
while game_count<5 and strike<3 and out<3 :
    game_count+=1
    strike = 0
    ball = 0
    num1,num2,num3 = map(int,input(f"시도 {game_count} : 입력한 숫자 - ").split())
    user_num_li = [num1,num2,num3]

    for i in range(3):
        if user_num_li[i]==pc_num_li[i]:
            strike+=1
        elif len([j for j in pc_num_li if j==user_num_li[i]])>0: #user_num_li[i] in pc_num_li
            ball+=1         
    if strike==0 and ball==0:
        out+=1
    out_msg = "" if out==0 else f", {out} Out"
    print(f"결과 : {strike} Strike , {ball} Ball {out_msg}\n")
msg_result = "승리" if strike==3 else f"패배 (시도 횟수 {game_count}회 초과)" if game_count==5 else f"패배 (Out 횟수 {out}회 초과)"
print(f"게임 종료 : {msg_result}\n정답 : {' '.join(map(str,pc_num_li))}")