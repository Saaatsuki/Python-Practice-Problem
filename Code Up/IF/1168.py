birth_number, gender_number = map(str, input("Please enter your resident registration number : ").split())

gender_number = int(gender_number)  # 入力を整数に変換

if gender_number == 1 or gender_number == 2:
    year = "19" + birth_number[0:2]
elif gender_number == 3 or gender_number == 4:
    year = "20" + birth_number[0:2]

if gender_number == 1 or gender_number == 3:
    gender = "MEN🥸"
elif gender_number == 2 or gender_number == 4:
    gender = "WOMEN😘"

import datetime
# 現在の日付と時刻を取得
current_date = datetime.datetime.now()
# 現在の年を取得
current_year = current_date.year

age = current_year - int(year)

msg = "You were born in {} and you were born on {}/{}, {} years old, and you are a {}"

print(msg.format(year, birth_number[2:4], birth_number[4:6], age, gender))


