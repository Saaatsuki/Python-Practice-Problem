import random

pc_ind_set = set()
while len(pc_ind_set)<3:
    pc_ind = random.randint(0,9)
    pc_ind_set.add(pc_ind)
pc_ind_li = list(pc_ind_set)

game_count = 0
strike = 0
ball = 0
out = 0

while strike<3 and game_count<5 and out<3:
    game_count+=1

    num1,num2,num3 = map(int,input(f"시도 {game_count} : 입력한 숫자 - ").split())
    user_li = [num1,num2,num3]
    strike = 0
    ball = 0
    for i in range(3):
        if pc_ind_li[i]==user_li[i]:
            strike+=1
        elif len([j for j in pc_ind_li if j==user_li[i]])>0:#user_li[i] in pc_ind_li
            ball+=1
    if strike==0 and ball==0:
        out+=1
    out_msg = "" if out==0 else f", {out} Out"
    print(f"결과 : {strike} Strike , {ball} Ball {out_msg}")
res_msg = "승리" if strike==0 else f"패배 (시도 횟수 {game_count}회 초과)" if game_count==5 else f"패배 (Out 횟수 {out}회 초과)"
print(f"게임 중료 : {res_msg}\n정답 : {' '.join(map(str,pc_ind_li))}")