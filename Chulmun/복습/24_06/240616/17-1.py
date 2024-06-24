import random

word_li = []
for i in ["첫","두","세"]:
    word = input(f"{i} 번째 단어를 입력하세요 : ")
    word_li.append(word)

com_word_ind = random.randint(0,2)
com_word = word_li[com_word_ind]
print(f"단어 선택 완료 게임 시작힙니다 . 선택된 단어 : {com_word}")
com_word_len = len(com_word)
com_word_li = list(com_word)

hide_count = com_word_len*0.5 if com_word_len%2==0 else com_word_len*0.5+0.5
hide_ind_set = set()
while len(hide_ind_set)<hide_count:
    hide_ind = random.randint(0,com_word_len-1)
    hide_ind_set.add(hide_ind)
hide_ind_li = list(hide_ind_set)

hide_word_li = com_word_li[:]
for i in hide_ind_li:
    hide_word_li[i]="_"

game_count = 0
while len([i for i in hide_word_li if i=="_"])>0:# "_" in hide_word_li
    game_count += 1
    alp = input(f"{game_count}번째 시도 , 아래 단어를 구성하는 알파벳 한 개 입력하세요\n{''.join(hide_word_li)}\n")
    count = 0
    for i in hide_ind_li:
        if com_word_li[i]==alp:
            hide_word_li[i]=alp
            count+=1
    print(f"단어에 포함되지 않은 알파벳 입니다.") if count==0 else print(f"입력한 알파벳 단어 내 포함 : {count}글자")
print(f"Clear!! - 선택된 단어 : {com_word} 총 시도 횟수 : {game_count}")