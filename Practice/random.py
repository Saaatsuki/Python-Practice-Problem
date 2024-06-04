# 整数を使用者から3つ受け取る
# １番目の数字：ランダムの範囲のスタート
# ２番目の数字：ランダムの範囲の最後
# ３番目の数字：ランダムで選ぶ個数

import random

def randomGet(start,end,select):

    random_list = []
    for i in range(start,end+1):
        random_list.append(i)
        
    result = random.choices(random_list,k=select)
    return result
    
numbers = []
for i in range(3):
    number = int(input(f"{i+1}番目の整数を入力してください："))
    while not (0<=number):
        input_number = int(input("0以上の整数を入力してください："))
    numbers.append(number)

randomGet(numbers[0],numbers[1],numbers[2])