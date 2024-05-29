import random

numbers100 = []

for i in range(1,101):
    numbers100.append(i)

random_number = random.choice(numbers100)

game_count = 0

msg = "더 {} 숫자 입니다"
msg_end = "게임이 끝났습니다"

while (game_count < 10):
    game_count += 1
    user_number = int(input(f"기회 {game_count}/10 1부터 100사이의 숫자를 맞춰보세요 (종료하려면 0 입력) : " ))
    
    if user_number==0:
        break
    
    while not (0<user_number<101):
       user_number =int(input("1-100를 입력해야지!! :"))
       
    if random_number == user_number:
        print("정답입니다!!!")
        break
    elif random_number > user_number:
        print(msg.format("큰")) 
    else:
        print(msg.format("작은"))
        
if game_count >= 10 and random_number != user_number:
    print(f"모든 기회를 사용하였습니다. 정답은 {random_number}입니다.")


print(msg_end)