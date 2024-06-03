import random

# 重複のないランダムな整数のリストを生成する関数
def numbers_without_duplicates(number):
    random_numbers = []  # 生成されるランダムな整数が格納されるリスト
    count = 0  # 生成されたランダムな整数の数を数える変数


    while count < number:
        random_number = random.randint(1, 100)  # 1から100までのランダムな整数を生成

        duplicate = False  # 重複のフラグを初期化
        for num in random_numbers:
            if num == random_number:
                duplicate = True  # 重複があればフラグを立てる
                break
        
        if not duplicate:  # 重複がない場合のみリストに追加
            random_numbers.append(random_number)
            count += 1  # 生成された整数の数を増やす
    return random_numbers  # 重複のないランダムな整数のリストを返す
        
# 生成するランダムな整数の数をユーザーに入力してもらう
number = int(input("Nの値を入力してください（1-100）: "))

if (0 < number <= 100):
    # numbers_without_duplicates 関数を呼び出して重複のないランダムな整数のリストを生成
    random_numbers = numbers_without_duplicates(number)
    print("生成されたリスト: ", random_numbers)
    
    # ユーザーにリスト内の要素を選択させる
    while True:
        index_number = int(input("選択したい要素のインデックスを入力してください（0-" + str(number-1) + "）: "))
        
        # ユーザーが有効なインデックスを入力した場合、対応する要素を表示
        if (0 <= index_number < number):
            print("選択した要素: ", random_numbers[index_number])
            break
        else:
            print("エラー: 有効なインデックスの範囲を超えています。")
            continue
else:
    print("Nは1以上100以下の整数でなければなりません。")
