import random
user_word_li = []
for i in ["첫","두","세"]:
    user_word = input(f"{i} 번째의 단어를 입력하세요▽\n")
    while not 3<= len(user_word)<=20:
        user_word = input(f"3이상 20이하 글자로 구성된 {i} 번째의 단어를 입력하세요▽\n")
    user_word_li.append(user_word)

pc_sel_index = random.randint(0,2)
pc_sel = user_word_li[pc_sel_index]
pc_sel_li = list(pc_sel)
pc_sel_len = len(pc_sel)
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어 : {pc_sel}")

bli_count = pc_sel_len*0.5 if pc_sel_len%2==0 else pc_sel_len*0.5+0.5
bli_ind_set = set()
while len(bli_ind_set)<bli_count:
    bli_ind = random.randint(0,pc_sel_len-1)
    bli_ind_set.add(bli_ind)
bli_ind_li = list(bli_ind_set)

pc_sel_bli_li = pc_sel_li[:]
for i in bli_ind_li:
    pc_sel_bli_li[i]="_"
game_count = 0
while len([i for i in pc_sel_bli_li if i == "_"]) > 0:#"_" in pc_sel_bli_li:
    game_count+=1
    user_alp = input(f"{game_count} 번째 시도 : 아레 단어를 구성하는 알파벳 한개 입력하세요.\n{''.join(pc_sel_bli_li)}\n")
    count = 0
    for i in bli_ind_li:
        if pc_sel_li[i]==user_alp:
            pc_sel_bli_li[i]=user_alp
            count=+1           
    if 0<count:
        msg = f"입력한 알파벳 단어 내 포함 : {count}"
    else:
        msg = "단어 내 포함되지 않은 알파벳입니다."
    print(msg)
print(f"Clear - 선택된 단어 : {pc_sel} , 총 시도 횟수 : {game_count}")