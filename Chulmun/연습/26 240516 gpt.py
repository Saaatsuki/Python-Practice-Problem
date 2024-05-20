import random

def generate_unique_numbers():
    # 0から9までの整数の中から重複しない3つの数字をランダムに選ぶ関数
    return random.sample(range(10), 3)

def get_strike_and_ball(guess, answer):
    # ユーザーの入力(guess)と正解の数(answer)を比較し、ストライクとボールの数を計算する関数
    strike = 0  # ストライクの数を初期化
    ball = 0    # ボールの数を初期化
    
    for i in range(3):
        # ユーザーの入力と正解の各桁を比較
        if guess[i] == answer[i]:
            strike += 1  # 桁と数字が両方一致している場合はストライク
        elif guess[i] in answer:
            ball += 1    # 数字は一致しているが桁が違う場合はボール
    
    return strike, ball  # ストライクとボールの数を返す

def main():
    # ゲームのメイン関数
    computer_numbers = generate_unique_numbers()  # コンピューターが選んだ正解の3つの数字を生成
    attempts = 0  # ユーザーが試みた回数を初期化
    strikes_out = 0  # ストライクアウトの回数を初期化

    print("野球ゲームを始めます！0-9の間の整数を3つ入力してください。")

    while attempts < 5 and strikes_out < 2:
        # ゲームループ: 試行回数が5回未満かつストライクアウトが2回未満の場合に継続
        try:
            user_input = input(f"試み {attempts + 1} : 入力した数字 - ")
            # ユーザーの入力を取得し、スペースで分割してリストに変換
            user_numbers = [int(digit) for digit in user_input.split()]

            if len(user_numbers) != 3 or len(set(user_numbers)) != 3:
                # 入力が3つの重複しない整数でない場合、エラーメッセージを表示し再入力を促す
                print("数字は重複しない3つの整数でなければなりません。もう一度試してください。")
                continue

            attempts += 1  # 試行回数をカウント
            strike, ball = get_strike_and_ball(user_numbers, computer_numbers)  # ストライクとボールの数を計算

            if strike == 3:
                # 3ストライクの場合、ユーザーの勝利
                print(f"結果 : {strike} Strike , {ball} Ball")
                print("ゲーム終了 : 勝利")
                print(f"正解 : {' '.join(map(str, computer_numbers))}")
                return  # ゲームを終了
            elif strike == 0 and ball == 0:
                # ストライクもボールもない場合、ストライクアウト
                print(f"結果 : {strike} Strike , {ball} Ball , Out")
                strikes_out += 1  # ストライクアウトの回数をカウント
            else:
                # それ以外の場合、結果を表示
                print(f"結果 : {strike} Strike , {ball} Ball")

        except ValueError:
            # 入力が無効な場合のエラーハンドリング
            print("入力が無効です。0から9の間の整数をスペースで区切って3つ入力してください。")

    # 5回の試行が終了したか、2回のストライクアウトでゲームオーバー
    print("ゲーム終了 : 敗北（試用回数5回を超える）")
    print(f"正解 : {' '.join(map(str, computer_numbers))}")

if __name__ == "__main__":
    main()  # スクリプトが直接実行された場合にゲームを開始
