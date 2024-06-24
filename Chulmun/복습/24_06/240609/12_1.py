import random

janken_list = ["가위","바위","보"]
pc_choice_num = random.randint(0,2)

user_choice = input("가위 바위 보 중 하나 입력하세요 : ")
while not user_choice=="가위" and not user_choice=="바위" and not user_choice=="보":
    user_choice = input("가위 바위 보 아닙니다.\n가위 바위 보 중 하나 입력하세요 : ") 

user_choice_num= janken_list.index(user_choice)

judge = pc_choice_num - user_choice_num

if judge == 0:
    msg = "무승부입니다!!"
elif  judge == 1 or judge == -2:
    msg = "당신이 졌습니다!!"
else:
    msg = "당신이 이겼습니다!!"

print(f"컴퓨터 선택 : {janken_list[pc_choice_num]}\n결과 : {msg}")