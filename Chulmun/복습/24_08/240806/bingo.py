import random

def output_bingo(argList, size):
    for i in range(size):
        for j in range(size):
            print(f"{argList[i * size + j]:2}", end=" ")
        print()

def count_bingos(bingo_list, size):
    bingos = 0

    # Check rows and columns
    for i in range(size):
        if all(bingo_list[i * size + j] == " *" for j in range(size)):
            bingos += 1
        if all(bingo_list[j * size + i] == " *" for j in range(size)):
            bingos += 1

    # Check diagonals
    if all(bingo_list[i * size + i] == " *" for i in range(size)):
        bingos += 1
    if all(bingo_list[i * size + (size - 1 - i)] == " *" for i in range(size)):
        bingos += 1

    return bingos

size = int(input("3~6의 숫자를 입력해주세요 : "))
while not 3 <= size <= 6:
    size = int(input("3~6의 숫자를 입력해주세요 : "))

bingo_num_li_len = size * size
bingo_num_li = []

while len(bingo_num_li) < bingo_num_li_len:
    bingo_num = random.randint(1, 36)
    if bingo_num not in bingo_num_li:
        bingo_num_li.append(bingo_num)

print("\n👾BINGO👾")
output_bingo(bingo_num_li, size)

bingo_cou = 0
while bingo_cou < 3:
    num = int(input("\n숫자를 입력해주세요 : "))
    while num not in bingo_num_li:
        num = int(input("BINGO안에 입력한 숫자 없습니다.\n다시 숫자를 입력해주세요 : "))

    idx = bingo_num_li.index(num)
    bingo_num_li[idx] = " *"
    output_bingo(bingo_num_li, size)
    
    bingo_cou = count_bingos(bingo_num_li, size)
    print(f"\n현재 빙고 수: {bingo_cou}")

print("\n3개의 빙고를 완성했습니다! 게임을 종료합니다.")