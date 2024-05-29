# random을 import 한다
import random

# 1-100의 숫자를 보관하는 리스트
numbers100 = []
for i in range(1,101):
    numbers100.append(i)

# 리스트의 안에 부터 랜덤으로 선택    
random_number = random.choice(numbers100)

msg = "더 {} 숫자 입니다"

# 만약에 random_number랑 user_number가 같은 숫자이라면 정답 
while True:
    user_number = int(input("1부터 100사이의 숫자를 맞춰보세요 : "))

    while not (1 <= user_number <= 100):
        user_number = int(input("1부터 100사이의 숫자 아닙니다.1부터 100사이의 숫자를 맞춰보세요 : "))

    if random_number == user_number:
        print("정답입니다!!!")
        break
    elif random_number > user_number:
        print(msg.format("큰")) 
        
    else:
        print(msg.format("작은"))
