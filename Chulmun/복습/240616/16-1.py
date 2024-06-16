import random

com_num_set = set()
while len(com_num_set)<3:
    com_num = random.randint(0,9)
    com_num_set.add(com_num)
com_num_li = list(com_num_set)
com_num = " ".join(map(str,com_num_li))

game_counnt = 0
strike = 0
ball = 0
out = 0

while game_counnt<5 and strike<3 and out<3 :
    game_counnt+=1
    strike = 0
    ball = 0
    num1,num2,num3 = map(int,input(f"시도 {game_counnt} : 입력한 숫자 - ").split())
    user_num_li = [num1,num2,num3]

    for i in range(0,2):
        if com_num_li[i]==user_num_li[i]:
            strike+=1
        elif len([j for j in com_num_li if j==user_num_li[i]])>0:
            ball +=1
    if strike==0 and ball==0:
        out += 1
    out_msg = f", {out} Out"  if not out==0 else ""
    print(f"결과 : {strike} Strike , {ball} Ball {out_msg}")
msg = "승리" if strike==3 else f"패배 (game count:{game_counnt})" if game_counnt==5 else f"패배 (Out:{out})"
print(f"GAME END : {msg}\nANSWER : {com_num}")