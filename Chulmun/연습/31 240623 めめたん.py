# 対象となる文字列を設定
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 文字列を単語ごとに分割し、リストに格納
msg_li = sentence.split()
msg_li = [i for i in msg_li]

# 改行を除いた文字列を文字ごとに分割し、リストに格納
cher_li = sentence.replace(" ","")
cher_li = [j for j in cher_li]

# 特定の文字列の位置を検索する関数を定義
def num_msg(msg):
    li = []  # 位置を格納するリスト
    m = ""   # 一時的に単語を構築するための変数
    n = 0    # 改行の数をカウントするための変数
    for i in range(len(sentence)):
        m += sentence[i]
        # 単語の終わり（スペースまたは改行）で、構築中の単語が検索対象と一致するか確認
        if (sentence[i] == " " and (m.replace(" ","")) == msg) or (sentence[i] == "\n" and (m.replace("\n","")) == msg) :
            # 一致する場合、その位置を計算してリストに追加
            l = (i - (len(m)-1) + (4 * n))
            li.append(l)
        # スペースまたは改行があった場合、一時的な単語のリセットと改行のカウントを行う
        if sentence[i] == "\n" or sentence[i] == " ":
            if sentence[i] == "\n":
                n += 1
            m = ""
    # 最後の単語が一致するか確認
    if m == msg:
        l = i - (len(m)-1)+ (4 * n)
        li.append(l)
    return li, n

# ユーザーに検索する文字列を入力させるループ
while True:
    input_msg = input("検索する文字列を入力してください: ")
    # 入力された文字列が何回出現するかをカウント
    c = 0
    for m in msg_li:
        if m == input_msg:
            c += 1
    # 出現回数を表示し、ループを抜ける
    if c > 0:
        print("検索された文字列の個数:", c)
        break
    # 一致する文字列が見つからなかった場合、再入力を促す
    print("該当する文字列がありません。もう一度入力してください。")

# 入力された文字列の位置と改行数を取得し表示
li, n = num_msg(input_msg)
print("検索された文字列の位置:", li)

# 単語数と改行を除いた文字数を計算し表示
print(f"単語の個数: {len(msg_li)}\n全体の文字数: {len(cher_li)-n}")
print("行数:", n + 1)