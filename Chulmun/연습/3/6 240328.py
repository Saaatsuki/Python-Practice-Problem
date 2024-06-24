# 週当たりの授業時間(時数/週)
hours_per_week = int(input("Please enter the class hours per week (hours/week)🙈:"))
# 欠席した総時間
absence_hours = int(input("Please enter the total number of hours you were absent🙉:"))
# 遅刻回数
tardy_ciunt = int(input("Please enter the number of times you are late🙊:"))

# 総授業時間の計算
# 週ごとの授業時間を週数で15倍して総授業時間を計算
total_class_hours = hours_per_week*15 

# 欠席時間による出席点数の計算
attendance_score = 20 - (20*absence_hours/total_class_hours)

# 遅刻回数と欠席時間
# 遅刻が3回以上あれば1時間の欠席時間として追加suru
if tardy_ciunt >= 3:
    absence_hours += 1

# 欠席時間による出席点数の計算
# まず、20点から始めます。これは満点の出席点数です。
# 欠席時間の割合を計算します。これは、欠席時間を総授業時間で割った値です。
# 欠席時間の割合を20から引き、出席点数を減らします。
# ただし、出席点数は負の値にはなりません。最小値は0です。
attendance_score = max(0, 20 - (20 * absence_hours / total_class_hours))

#欠席時間が総授業時間の4分の1を超える場合は、F（不合格）を出力させる
if absence_hours > total_class_hours/4:
    print("F (Credit not granted)🐼")
else:
    print("🐰Your attendance score is",round(attendance_score,2))