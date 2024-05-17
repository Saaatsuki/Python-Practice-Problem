import random

def generate_unique_numbers():
    return random.sample(range(10), 3)

def get_strike_and_ball(guess, answer):
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball

def main():
    computer_numbers = generate_unique_numbers()
    attempts = 0
    strikes_out = 0

    print("野球ゲームを始めます！0-9の間の整数を3つ入力してください。")

    while attempts < 5 and strikes_out < 2:
        try:
            user_input = input(f"試み {attempts + 1} : 入力した数字 - ")
            user_numbers = [int(digit) for digit in user_input.split()]

            if len(user_numbers) != 3 or len(set(user_numbers)) != 3:
                print("数字は重複しない3つの整数でなければなりません。もう一度試してください。")
                continue

            attempts += 1
            strike, ball = get_strike_and_ball(user_numbers, computer_numbers)

            if strike == 3:
                print(f"結果 : {strike} Strike , {ball} Ball")
                print("ゲーム終了 : 勝利")
                print(f"正解 : {' '.join(map(str, computer_numbers))}")
                return
            elif strike == 0 and ball == 0:
                print(f"結果 : {strike} Strike , {ball} Ball , Out")
                strikes_out += 1
            else:
                print(f"結果 : {strike} Strike , {ball} Ball")

        except ValueError:
            print("入力が無効です。0から9の間の整数をスペースで区切って3つ入力してください。")

    print("ゲーム終了 : 敗北（試用回数5回を超える）")
    print(f"正解 : {' '.join(map(str, computer_numbers))}")

if __name__ == "__main__":
    main()
