score_math = float(input("Please enter your test score for math : "))
score_science = float(input("Please enter your test score for science : "))
score_english = float(input("Please enter your test score for english : "))

# 3つのテストの平均スコアを計算する
avarage = sum({score_math,score_science,score_english}) / len({score_math,score_science,score_english})

# 平均スコアに応じて評価を表示するメッセージを準備する
msg = "The average is {:.2f} points. Your evaluation is {}🐼"

if (90 <= avarage):
    print(msg.format(avarage,"A"))
elif (80 <= avarage < 90):
    print(msg.format(avarage,"B"))
elif (70 <= avarage < 80):
    print(msg.format(avarage,"C"))
elif (60 <= avarage < 70):
    print(msg.format(avarage,"D"))
elif (avarage < 60):
    print(msg.format(avarage,"F"))