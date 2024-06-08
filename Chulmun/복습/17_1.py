import random

input_word_list = []
for i in ["첫", "두", "세"]:
    input_word = input(f"{i} 번째 단어를 입력 하세요\n")
    input_word_len = len(input_word)
    while not 3 <= input_word_len <= 20:
        input_word = input(f"3이상 20이하 글자로 구성된 단어를 입력 하세요\n")
        input_word_len = len(input_word)
    input_word_list.append(input_word)

pc_select_word_index = random.randint(0, 2)
pc_select_word = input_word_list[pc_select_word_index]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어 : {pc_select_word}")
pc_select_word_list = list(pc_select_word)

blind_count = int(input_word_len * 0.5) if input_word_len % 2 == 0 else int(input_word_len * 0.5 + 0.5)

blind_char_index_set = set()
while len(blind_char_index_set) < blind_count:
    blind_char_index = random.randint(0, input_word_len - 1)
    blind_char_index_set.add(blind_char_index)

pc_select_word_blind_list = pc_select_word_list.copy()
for i in blind_char_index_set:
    pc_select_word_blind_list[i] = "_"
pc_select_word_blind = "".join(pc_select_word_blind_list)

game_count = 0
in_count = 0
while "_" in pc_select_word_blind_list:
    game_count += 1
    game_input = input(f"{game_count}번째 시도 , 아래 단어를 구성하는 알파벳 한개 입력하세요.\n{pc_select_word_blind}\n")

    in_word_tf = False
    for i in pc_select_word:
        if game_input == i:
            in_word_tf = True

    if in_word_tf: # game_input in pc_select_word
        for i in range(len(pc_select_word)):
            if pc_select_word[i] == game_input and pc_select_word_blind_list[i] == "_":
                pc_select_word_blind_list[i] = game_input
                in_count += 1
                msg = f"입력한 알파벳 단어 내 포함 : {in_count}"
                break
        else:
            msg = "단어 내 포함되지 않은 알파벳입니다"
    else:
        msg = "단어 내 포함되지 않은 알파벳입니다"

    print(msg)
    pc_select_word_blind = "".join(pc_select_word_blind_list)

print(f"Clear!!! 선택된 단어 : {pc_select_word} , 총 시도 횟수 : {game_count}")
