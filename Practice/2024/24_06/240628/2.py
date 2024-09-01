import random

def getRandomNum(arg_num):
    """빙고의 숫자를 랜덤으로 뽑아주는 함수"""
    n = arg_num ** 2
    
    num_list = []
    while len(num_list) < n:
        num = random.randint(1, 36)
        if num not in num_list:
            num_list.append(num)
    
    return num_list

def printBingo(arg_num, arg_list):
    """빙고의 보드판을 출력하는 함수"""

    for i in range(arg_num):
        for j in range(arg_num):
            # print(f'{arg_list[i * arg_num + j]:2d}', end=" ")
            print(arg_list[i * arg_num + j] if arg_list[i * arg_num + j] >= 10 else f' *' if arg_list[i * arg_num + j] == 0 else f' {arg_list[i * arg_num + j]}', end=" ")

        print()

def checkNumber(arg_num, arg_list):
    for i in range(len(arg_list)):
        if arg_list[i] == arg_num:
            arg_list[i] = 0

def checkBingo(arg_num, arg_list):

    bingo = 0
    
    # 横、縦
    for i in range(arg_num):
        bingo1 = 0
        bingo2 = 0
        
        for j in range(arg_num):
            bingo1 += arg_list[j * arg_num + i]
            bingo2 += arg_list[j + i * arg_num]    
        
        if bingo1 == 0:
            bingo += 1
        if bingo2 == 0:
            bingo += 1

    # 斜め
    # 3 : 2 4 6
    # 4 : 3 6 9 12
    # 5 : 4 8 12 16 20

    bingo3 = 0
    bingo4 = 0
    for i in range(arg_num):
        bingo3 += arg_list[i * (arg_num + 1)]
        bingo4 += arg_list[(arg_num - 1) * (i + 1)]

    if bingo3 == 0:
        bingo += 1
    if bingo4 == 0:
        bingo += 1

    return bingo

        


board_size = int(input("Enter the size of the vingo board (3 to 6): "))

while not (3 <= board_size <= 6):
    print("Size must be between 4 and 6. Please try again.")
    board_size = int(input("Enter the size of the vingo board (3 to 6): "))

num_list = getRandomNum(board_size)

printBingo(board_size, num_list)

count = 0
while True:
    count += 1
    user_num = int(input(f"Press Enter to generate a random number:\nRandom Number {count}: "))

    checkNumber(user_num, num_list)

    printBingo(board_size, num_list)

    if checkBingo(board_size, num_list) >= 2:
        break

print("Congratulations!! You've won the game with 2 or more bingos !!")