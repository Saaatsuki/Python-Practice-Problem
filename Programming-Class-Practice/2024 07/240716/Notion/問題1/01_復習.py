from prettytable import PrettyTable

# 学生の名前と得点を含む辞書
students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 90,
    'Eva': 95
}

# 得点でソート（昇順）
students_sorted1 = sorted(students.items(), key=lambda x: x[1])
print(students_sorted1)

# 得点でソート（降順）
students_sorted2 = sorted(students.items(), key=lambda x: x[1], reverse=True)
print(students_sorted2)

# 上位3名を取得
top3 = students_sorted2[:3]

# PrettyTableを使用して表を作成
table1 = PrettyTable(["name", "score"])
table2 = PrettyTable([" ", "name", "score"])

# 上位3名のデータを表に追加
for name, score in top3:
    table1.add_row([name, score])

# 全員のデータをランキング順に表に追加
for ranking, (name, score) in enumerate(students_sorted2, start=1):
    table2.add_row([ranking, name, score])

# 表を出力
print(table1)
print(table2)
