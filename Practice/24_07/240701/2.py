import random

def randomSample(argList, argK):
    if len(argList) < argK:
        raise ValueError("Sample size cannot be larger than the list.")

    sample = []
    argList_copy = argList[:]
    for _ in range(argK):
        index = random.randint(0, len(argList_copy) - 1)
        sample.append(argList_copy.pop(index))
    return sample

def getJoin(argList, argSep):
    join = ""
    index = 0
    while index < len(argList):
        join += f"{argList[index]:2d}" if argList[index] != 0 else "* "
        index += 1
        if index < len(argList):
            join += argSep
    return join

def bingoPrint(argList, argK):
    index = 0
    for _ in range(argK):
        print(getJoin(argList[index:index + argK], ' '))
        index += argK

def getAll(argList):
    for val in argList:
        if val != 0:
            return False
    return True

def checkBingo(board, size):
    bingo_count = 0

    for i in range(size):
        if getAll(board[i * size:(i + 1) * size]):
            bingo_count += 1

    for i in range(size):
        if getAll([board[j * size + i] for j in range(size)]):
            bingo_count += 1

    if getAll([board[i * size + i] for i in range(size)]):
        bingo_count += 1

    if getAll([board[i * size + (size - 1 - i)] for i in range(size)]):
        bingo_count += 1
    return bingo_count

size = int(input("Enter the size of the bingo board (3-6): "))
while not 3 <= size <= 6:
    size = int(input("Size must be between 3 and 6. Please try again.\nEnter the size of the bingo board: "))

sizeXsize = size ** 2
bingo_number_li = randomSample([num for num in range(1, 37)], sizeXsize)

print("Initial Bingo Board:")
bingoPrint(bingo_number_li, size)

game_count = 0
while True:
    game_count += 1
    print("Press Enter to generate a random number:")
    user_num = int(input(f"Random Number {game_count}: "))

    if user_num not in range(1, 37):
        print("Invalid number. Please enter a number between 1 and 36.")
        continue

    for i in range(len(bingo_number_li)):
        if bingo_number_li[i] == user_num:
            bingo_number_li[i] = 0

    print("Current Bingo Board:")
    bingoPrint(bingo_number_li, size)

    if checkBingo(bingo_number_li, size) > 1: 
        break

print("Congratulations!! You've won the game with 2 or more bingos!!")