def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
   
    # """
    # 出席点数を計算する関数

    # Parameters:
    #     hours_per_week (int): 週当たりの授業時間（時数）
    #     absence_hours (int): 欠席した総時間
    #     tardy_count (int): 遅刻回数

    # Returns:
    #     float: 出席点数
    #     この値は、学生の出席状況を数値化したもので、0から20の範囲で表されます。
    #     出席状況が良いほど高い値となります。
    # """
    
    # 総授業時間の計算
    total_class_hours = hours_per_week * 15 

    # 遅刻が3回以上あれば1時間の欠席時間として追加
    if tardy_count >= 3:
        absence_hours += 1

    # 出席点数の計算
    attendance_score = max(0, 20 - (20 * absence_hours / total_class_hours))

    return attendance_score

# 週当たりの授業時間(時数/週)
hours_per_week = int(input("Please enter the class hours per week (hours/week)🙈:"))
# 欠席した総時間
absence_hours = int(input("Please enter the total number of hours you were absent🙉:"))
# 遅刻回数
tardy_count = int(input("Please enter the number of times you are late🙊:"))

# 出席点数の計算
attendance_score = calculate_attendance_score(hours_per_week, absence_hours, tardy_count)

# 欠席時間が総授業時間の4分の1を超える場合は、F（不合格）を出力
if absence_hours > hours_per_week * 15 / 4:
    print("F (Credit not granted)🐼")
else:
    print("🐰Your attendance score is", round(attendance_score, 2))
