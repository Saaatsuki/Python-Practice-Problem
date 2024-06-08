import random

# 単語の入力
input_word_li = []
for i in ["첫", "두", "세"]:
    input_word = input(f"{i}번째의 단어를 입력하세요\n")
    input_word_len = len(input_word)
    while not 3 <= input_word_len <= 20:
        input_word = input("3이상 20이하의 단어를 입력하세요\n")
        input_word_len = len(input_word)
    input_word_li.append(input_word)

# ランダムに単語を選択
input_word_li_index = random.randint(0, len(input_word_li) - 1)
pc_sel_word = input_word_li[input_word_li_index]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {pc_sel_word}")

# 選択された単語をリストに変換
pc_sel_word_li = list(pc_sel_word)
pc_sel_word_len = len(pc_sel_word)

# 隠す文字の数を決定
hide_count = int(pc_sel_word_len * 0.5) if pc_sel_word_len % 2 == 0 else int(pc_sel_word_len * 0.5 + 0.5)

# 隠すインデックスをセットに追加
hide_index_set = set()
while len(hide_index_set) < hide_count:
    hide_index = random.randint(0, pc_sel_word_len - 1)
    hide_index_set.add(hide_index)

# インデックスをリストに変換
hide_index_li = list(hide_index_set)

# 選択されたインデックスを隠す
for i in hide_index_li:
    pc_sel_word_li[i] = "_"
pc_sel_word_join = "".join(pc_sel_word_li)

# ゲームの開始
hide_tf = False
game_count = 0

while not hide_tf:
    game_count += 1
    input_alp = input(f"{game_count} 시도: 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{pc_sel_word_join}\n")
    
    # ユーザーの入力をチェックして単語を更新
    for i in range(pc_sel_word_len):
        if pc_sel_word[i] == input_alp:
            pc_sel_word_li[i] = input_alp
    
    pc_sel_word_join = "".join(pc_sel_word_li)
    
    # すべての文字が表示されたかをチェック
    hide_tf = "_" not in pc_sel_word_li

print(f"게임 종료! 선택된 단어는: {pc_sel_word} 맞혔습니다!")
