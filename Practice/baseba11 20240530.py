import random

number10_list = []
for i in range(1,10):
    number10_list.append(i)

pc_random_number = random.sample(number10_list,3)
# while len(random_numbers)<3:
#     random_number = random.randint(0,9)
#     flag = True
#     for i in range(3):
#         if i == random_number:
#             flag = False
#     if flag:
#         random_numbers.append(random_number)
pc_random_number_output = ' '.join(map(str, pc_random_number))
print(pc_random_number_output)

game_count = 1
strike = 0
ball = 0
out = 0

while (game_count <= 5 and strike < 2):
    strike = 0
    ball = 0
    user_number1,user_number2,user_number3 = map(int,input(f"시도 {game_count} : 입력한 숫자 : ").split())
    while not (0<=user_number1<=9):
        user_number1 = int(input("첫번째 정수(0-9)를 입력 해주세요 :" ))   
    while not (0<=user_number2<=9):
        user_number2 = int(input("두번째 정수(0-9)를 입력 해주세요 :" ))    
    while not (0<=user_number3<=9):
        user_number3 = int(input("세번째 정수(0-9)를 입력 해주세요 :" ))

    user_numbers_list = [user_number1,user_number2,user_number3]
    print(" ".join(map(str,user_numbers_list)))

    for pc_random_index in range(3):
        for user_number_index in range(3):
            if pc_random_number[pc_random_index] == user_numbers_list[user_number_index]:
                if pc_random_index == user_number_index:
                    strike += 1
                else:
                    ball += 1
    
    if ball ==0 and strike ==0:
        out += 1
    
    game_count += 1
    
    print(f"결과 : {strike} strike , {ball} ball , {out} out")

if strike==3:
    game_result = "승리!!"
else:
    game_result = f"패배 (시도 횟수 {game_count}회 초과)"

print(f"게임 충료 : {game_result}")
print(f"정답 : {pc_random_number_output}")