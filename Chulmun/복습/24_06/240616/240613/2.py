import random
word_li = []
for i in ["첫","두","세"]:
    word = input(f"{i} 번째 단어를 입력하세요\n")
    while not 3<=len(word)<=20:
        word = input(f"3이상 20이하 글자로 구성된 {i} 번째 단어를 입력하세요\n")
    word_li.append(word)

pc_sel_ind = random.randint(0,2)
pc_sel = word_li[pc_sel_ind]
pc_sel_li = list(pc_sel)
pc_sel_len = len(pc_sel_li)
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어 : {pc_sel}")

hide_count = pc_sel_len*0.5 if pc_sel_len%2==0 else pc_sel_len*0.5+0.5
hide_ind_set = set()
while len(hide_ind_set)<hide_count:
    hide_ind = random.randint(0,pc_sel_len-1)
    hide_ind_set.add(hide_ind)
hide_ind_li = list(hide_ind_set)

hide_pc_sel_li = pc_sel_li[:]
for i in hide_ind_li:
    hide_pc_sel_li[i]="_"
game_count = 0
while len([i for i in hide_pc_sel_li if i=="_"])>0: #"_" in hide_pc_sel_li
    game_count +=1
    alp = input(f"{game_count}번째 시도 : 아개 단어를 구성하는 알파벳 한개 입력하세요.\n{' '.join(hide_pc_sel_li)}\n")
    count = 0
    for i in hide_ind_li:
        if pc_sel_li[i] == alp :
            hide_pc_sel_li[i] = alp
            count +=1
    if count>0:
        msg = f"입력한 알파벳 단어 내 포함 : {count}글자"
    else:
        msg = "단어 내 포함되지 않은 알파벳입니다."
    print(msg)
print(f"Clear - 선택된 단어 : {pc_sel} , 총 시도 횟수 : {game_count}")