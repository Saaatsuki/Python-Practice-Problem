import random
aiko = 0
pc_win = 0
user_win = 0
while pc_win<2 and user_win<2:
    janken_li = ["가위","바위","보"]
    # user_jan = input(f"{janken_li[0]},{janken_li[1]},{janken_li[2]} 충 하나를 입력하세요. : ")
    user_jan = input(f'{",".join(janken_li)} 중 하나를 입력하세요. : ')
    while not user_jan=="가위" and not user_jan=="바위" and not user_jan=="보":
        user_jan = input(f"{','.join(janken_li)} 중에서 선택하세요. : ")

    user_jan_index = user_jan.index(user_jan)
    pc_jan_index = random.randint(0,2)
    pc_jan = janken_li[pc_jan_index]

    jan_result = pc_jan_index - user_jan_index

    if jan_result==0:
        aiko+=1
        msg = "무승부"
    elif jan_result==-2 or jan_result==1:
        pc_win+=1
        msg = "패배"
    else:
        user_win+=1
        msg = "승리"
    print(f"컴퓨터 : {pc_jan}\n{msg} 현재 전적 : {user_win}승 {pc_win}패 {aiko}무")
result = "컴퓨터" if pc_win==2 else "사용자"
print(f"전적 : {user_win}승 {pc_win}패 {aiko}무\n최종 승자 : {result}")