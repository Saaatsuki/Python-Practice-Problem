from prettytable import PrettyTable

output_li = ["이름", "국어", "영어", "수학", "총점", "평균", "등수"]

student_data = []

menu = 0

while menu != 4:
    print("\n[메뉴 선택]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 화면 출력")
    print("3. 학생 성적 파일 출력")
    print("4. 종료")

    menu = int(input("메뉴를 선택하세요 : "))

    if menu == 1:
        # 学生情報の入力
        name = input("학생 이름 : ")
        kokugo = int(input("국어 점수 : "))
        eng = int(input("영어 점수 : "))
        math = int(input("수학 점수 : "))
        
        # 合計と平均の計算
        test_sum = kokugo + eng + math
        test_avg = test_sum / 3
        
        # 学生データリストにデータを追加
        student_data.append([name, kokugo, eng, math, test_sum, f"{test_avg:.2f}", None])

    elif menu == 2:
        # 合計点で学生を降順にソート
        sorted_students = sorted(student_data, key=lambda x: x[4], reverse=True)
        
        # PrettyTableインスタンスを作成
        table = PrettyTable(output_li)
        
        # ソートされたデータでテーブルを作成
        for i, student in enumerate(sorted_students, start=1):
            table.add_row([student[0], student[1], student[2], student[3], student[4], student[5], i])
        
        # テーブルを表示
        print("[학생 성적 목록]")
        print(table)

    elif menu == 3:
        # 合計点で学生を降順にソート
        sorted_students = sorted(student_data, key=lambda x: x[4], reverse=True)
        
        # PrettyTableインスタンスを作成
        table = PrettyTable(output_li)
        
        # ソートされたデータでテーブルを作成
        for i, student in enumerate(sorted_students, start=1):
            table.add_row([student[0], student[1], student[2], student[3], student[4], student[5], i])
        
        # テーブルを表示
        print("[학생 성적 파일 출력]")
        print(table)

print("프로그램 종료")
