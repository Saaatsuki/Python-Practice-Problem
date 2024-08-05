import random

word_li = []
for i in ["첫", "두", "세"]:
    word = input(f"{i}번째 단어를 입력하세요 : ")
    while not 3 <= len(word) <= 20:
        word = input(f"3이상 20이하의 {i}번째 단어를 입력하세요 : ")
    word_li.append(word)

com_word_idx = random.randint(0, 2)
com_word = word_li[com_word_idx]

print(f"단어 선택 완료 게임을 시작합니다 : {com_word}")

com_word_len = len(com_word)
com_word_li = list(com_word)
hide_count = int(com_word_len * 0.5) if com_word_len%2==0 else int(com_word_len * 0.5 + 0.5)

hide_idx_li = []
while len(hide_idx_li) < hide_count:
    hide_idx = random.randint(0, com_word_len - 1)
    if hide_idx not in hide_idx_li:  
        hide_idx_li.append(hide_idx)

com_word_hide_li = com_word_li[:]
for i in hide_idx_li:
    com_word_hide_li[i] = "_"
hide_word = "".join(com_word_hide_li)

game_count = 0
while "_" in com_word_hide_li:
    game_count += 1
    hide_word = "".join(com_word_hide_li)
    inp_alp = input(f"{game_count}번째 시도 , 아래 단어를 구성하는 알파벳 한개 입력하세용 : \n{hide_word}\n\n")
    
    while len(inp_alp) != 1:  
        inp_alp = input(f"한 개의 알파벳을 입력하세요: ")

    alp_con = 0
    for i in hide_idx_li:
        if com_word[i] == inp_alp and com_word_hide_li[i] == "_":  
            com_word_hide_li[i] = inp_alp
            alp_con += 1
    
    if alp_con > 0:
        print(f"입력한 알파벳 단어 내 포함 : {alp_con} 글자")
    else:
        print("단어 내 포함하지 않은 알파벳입니다.")

print(f"Clear - 선택된 단어 : {com_word} , 시도 횟수 : {game_count}")
