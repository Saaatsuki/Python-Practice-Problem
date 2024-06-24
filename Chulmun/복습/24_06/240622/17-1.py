import random

def get_user_words():
    user_word_li = []
    for i in ["첫", "두", "세"]:
        user_word = input(f"{i} 번째 단어를 입력하세요\n")
        while not 3 <= len(user_word) <= 20:
            user_word = input(f"3글자 이상 20글자 이하로 구성된 {i} 번째 단어를 입력하세요\n")
        user_word_li.append(user_word)
    return user_word_li

def choose_hidden_indices(word_length):
    hide_count = int(word_length * 0.5) if word_length % 2 == 0 else int(word_length * 0.5) + 1
    hide_ind_set = set()
    while len(hide_ind_set) < hide_count:
        hide_ind = random.randint(0, word_length - 1)
        hide_ind_set.add(hide_ind)
    return list(hide_ind_set)

def play_game(pc_word, pc_word_li, hide_ind_li):
    pc_word_li_hide = pc_word_li[:]
    for i in hide_ind_li:
        pc_word_li_hide[i] = "_"
    
    game_count = 0
    
    while "_" in pc_word_li_hide:
        game_count += 1
        alp = input(f"{game_count}번째 시도. 아래 단어를 구성하는 알파벳 한개를 입력하세요.\n{''.join(pc_word_li_hide)}\n")
    
        inAlp_count = 0
        for i in hide_ind_li:
            if pc_word_li[i] == alp:
                pc_word_li_hide[i] = alp
                inAlp_count += 1
        if inAlp_count > 0:
            msg = f"입력한 알파벳은 단어 내에 포함됩니다. 포함된 글자 수: {inAlp_count}"
        else:
            msg = "단어 내에 포함되지 않은 알파벳입니다."
        print(msg)
    print(f"Clear! 선택된 단어 : {pc_word}, 시도 횟수 : {game_count}")

# メインのロジックをトップレベルに配置
user_word_li = get_user_words()
pc_word_ind = random.randint(0, 2)
pc_word = user_word_li[pc_word_ind]
pc_word_len = len(pc_word)
pc_word_li = list(pc_word)
print(f"단어 선택 완료. 게임을 시작합니다. 선택된 단어 : {pc_word}")

hide_ind_li = choose_hidden_indices(pc_word_len)
play_game(pc_word, pc_word_li, hide_ind_li)