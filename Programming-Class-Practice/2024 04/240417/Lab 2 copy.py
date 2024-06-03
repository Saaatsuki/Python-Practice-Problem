import random

success = False

while not success:
    # ① 使用者はまず生成するランダム整数の個数Nを入力します。
    number = int(input("Nの値を入力してください（1-100）："))
    random_numbers = []

    if 0 < number <= 100:
        for i in range(number):
            # ② 入力されたNに基づいて、1から100までの数字の中から重複しないN個のランダムな数字を生成します。
            random_number = random.randint(1, 100)
            # ③ 生成されたランダムな数字はリストに保存されます。
            random_numbers.append(random_number)

        print("生成されたリスト：", random_numbers)
        while True:
            # ④ 使用者にリストから選択した要素のインデックスを入力してもらいます。
            index_number = int(input("欲しい要素のインデックスを入力してください（0-" + str(number - 1) + "）："))

            # ⑤ プログラムは使用者が選択したインデックスに対応するリストの要素を出力します。
            if 0 <= index_number < number:
                print("選択したインデックスの要素：", random_numbers[index_number])
                break
            else:
                print("エラー：有効なインデックスの範囲を超えています。")
                continue
            
        success = True
    
    else:
        print("Nは1以上100以下の整数でなければなりません。")
        continue
