import random
# 3つの単語を受け取る
input_word_li = []
for i in ["첫", "두", "세"]:
    input_word = input(f"{i}번째 단어를 입력하세요\n")
    input_word_len = len(input_word)
    while not 3 <= input_word_len <= 20:
        input_word = input("3이상 20이하의 단어를 입력하세요\n")
        input_word_len = len(input_word)
    input_word_li.append(input_word)
input_word_li_len = len(input_word_li)

# 隠したい単語をランダムで選択
input_word_li_index = random.randint(0, input_word_li_len - 1)
pc_sel_word = input_word_li[input_word_li_index]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {pc_sel_word}")
pc_sel_word_li = list(pc_sel_word)
pc_sel_word_len = len(pc_sel_word)

# 単語の内隠したい文字をランダムセ選択
hide_count = int(pc_sel_word_len * 0.5) if pc_sel_word_len % 2 == 0 else int(pc_sel_word_len * 0.5 + 0.5)
hide_index_set = set()
while hide_count > len(hide_index_set):
    hide_index = random.randint(0, pc_sel_word_len - 1)
    hide_index_set.add(hide_index)
hide_index_li = list(hide_index_set)

# アンダーバーに変換
pc_sel_word_hide_li = pc_sel_word_li.copy()
for i in hide_index_li:
    pc_sel_word_hide_li[i] = "_"
pc_sel_word_hide_join = "".join(pc_sel_word_hide_li)

# ゲーム開始
game_count = 0
while "_" in pc_sel_word_hide_li:
    game_count += 1
    input_alp = input(f"{game_count} 시도: 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{pc_sel_word_hide_join}\n")
    count = 0
    for i in hide_index_li:
        if pc_sel_word_li[i] == input_alp:
            pc_sel_word_hide_li[i] = input_alp
            count += 1
    print(f"입력한 알파벳 단어 내 포함: {count} 글자") if count > 0 else print("단어 내 포함되지 않은 알파벳입니다.")  
    pc_sel_word_hide_join = "".join(pc_sel_word_hide_li)

print(f"Clear!!! 선택된 단어: {pc_sel_word}, 총 시도 횟수: {game_count}")