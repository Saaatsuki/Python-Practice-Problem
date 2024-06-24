import random

user_word_li = []
for i in ["첫", "두", "세"]:
    user_word = input(f"{i} 번째 단어를 입력하세요\n")
    while not 3 <= len(user_word) <= 20:
        user_word = input(f"3이상 20이하 글자로 구성된 단어를 입력하세요.\n")
    user_word_li.append(user_word)

pc_ran_ind = random.randint(0, 2)
pc_ran = user_word_li[pc_ran_ind]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {pc_ran}")

pc_ran_li = list(pc_ran)
pc_ran_len = len(pc_ran_li)

hide_count = pc_ran_len * 0.5 if pc_ran_len % 2 == 0 else pc_ran_len * 0.5 + 0.5
hide_ind_set = set()
while len(hide_ind_set) < hide_count:
    hide_ind = random.randint(0, pc_ran_len - 1)
    hide_ind_set.add(hide_ind)
hide_ind_li = list(hide_ind_set)
pc_ran_hide_li = pc_ran_li[:]
for i in hide_ind_li:
    pc_ran_hide_li[i] = "_"
pc_ran_hide = "".join(pc_ran_hide_li)
game_count = 0
while len([i for i in pc_ran_hide if i == "_"]) > 0:  # "_" in pc_ran_hide:
    game_count += 1
    user_alp = input(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{pc_ran_hide}\n")
    count = 0
    for i in hide_ind_li:
        if pc_ran_li[i] == user_alp:
            pc_ran_hide_li[i] = user_alp  
            count += 1
    if count > 0:
        msg = f"입력한 알파벳 단어 내 포함: {count}글자"
        pc_ran_hide = "".join(pc_ran_hide_li)
    else:
        msg = "단어 내 포함되지 않은 알파벳입니다."
    print(msg)
print(f"Clear!! - 선택된 단어: {pc_ran}, 총 시도 횟수: {game_count}")
