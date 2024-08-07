import random

def output_bingo(argList, masu):
    for i in range(masu):
        for j in range(masu):
            print(f"{argList[i * masu + j]:2}", end=" ")
        print()
        

masu = int(input("3~6의 숫자를 입력해주세요 : "))
while not 3<=masu<=6:
    masu = int(input("3~6의 숫자를 입력해주세요 : "))

bingo_num_li_len = masu * masu
bingo_num_li = []

while len(bingo_num_li) < bingo_num_li_len:
    bingo_num = random.randint(1,36)
    if bingo_num not in bingo_num_li:
        bingo_num_li.append(bingo_num)

output_bingo(bingo_num_li,masu)