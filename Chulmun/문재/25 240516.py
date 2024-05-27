import random

numbers = []

for i in range(10):
    numbers.append(i)
    

random_numbers = random.sample(numbers,3)
print(random_numbers)

str_random_numbers = " ".join(map(str,random_numbers))

out = 0
count = 0
ball = 0
strike = 0

while (count <= 5) and (out < 3) and (strike < 3):
    strike = 0
    ball = 0
    count += 1
    
    user_numbers = []
    for i in range(3):
        user_number = int(input(f"{i+1}番目の数字を入力してください\n"))
        user_numbers.append(user_number)
    
    
    print(random_numbers)
    print(user_numbers)
    
    for i in range(3):
        if random_numbers[i] == user_numbers[i]:
            strike += 1
        elif random_numbers[i] in user_numbers:
            ball += 1

    if strike == 0 and ball == 0:
        out += 1
    


    print(f"試行回数：{count} 入力した数字 - {str_random_numbers}")
    print(f"結果：{strike} strike!! , {ball} ball!! , {out} out!!!") 

if strike == 3:
    msg = "勝利！！"
else:
    msg = "ゲームオーバー！！"

print(f"ゲーム終了　：　{msg}")
print(f"正解：{str_random_numbers}")