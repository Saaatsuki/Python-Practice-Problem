# 平均スコアを計算して評価を表示する関数
def calculate_and_print_grade(score_math, score_science, score_english):
    # 3つのテストの平均スコアを計算する
    average = (score_math + score_science + score_english) / 3

    # 平均スコアに応じて評価を行う
    if (average >= 90):
        grade = "A"
    elif (80 <= average < 90):
        grade = "B"
    elif (70 <= average < 80):
        grade = "C"
    elif (60 <= average < 70):
        grade = "D"
    else:
        grade = "F"

    # 平均スコアを小数点以下2桁まで表示して評価を表示する
    print("The average is {:.2f} points. Your evaluation is {}🐼".format(average, grade))

# テストスコアをユーザーに入力してもらう
score_math = float(input("Please enter your test score for math："))
score_science = float(input("Please enter your test score for science："))
score_english = float(input("Please enter your test score for english："))

# 評価を計算して表示する関数を呼び出す
calculate_and_print_grade(score_math, score_science, score_english)
