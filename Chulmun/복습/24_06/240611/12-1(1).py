import random
janken_li = ["가위","바위","보"]

pc_sel_index = random.randint(0,len(janken_li)-1)
pc_sel = janken_li[pc_sel_index]

user_sel = input("가위,바위,보 중 하나를 선택하세요 : ")
while not user_sel in janken_li:
    user_sel = input(f"{user_sel}는 잘못된 입력입니다.\n가위,바위,보 중에세 하나를 선택하세요 : ")
user_sel_index = janken_li.index(user_sel)
janken_result = pc_sel_index - user_sel_index

if janken_result==0:
    result_msg = "무승부입니다!!"
elif janken_result==1 or janken_result==-2:
    result_msg = "당신이 졌습니다!"
else:
    result_msg = "당신이 이겼습니다!"
print(f"컴퓨터의 선택 : {pc_sel}\n결과 : {result_msg}")