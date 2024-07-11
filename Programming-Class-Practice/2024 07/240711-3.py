import csv
from prettytable import PrettyTable

school_li = []

with open('2024_std_num_high_school.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row["제외여부"] == "N":
            school = {
                '학교명': row['학교명'],
                '1학년(남)': int(row['1학년(남)']),
                '1학년(여)': int(row['1학년(여)']),
                '2학년(남)': int(row['2학년(남)']),
                '2학년(여)': int(row['2학년(여)']),
                '3학년(남)': int(row['3학년(남)']),
                '3학년(여)': int(row['3학년(여)']),
            }

            school['1학년 전채 학생 수'] = school['1학년(남)'] + school['1학년(여)']
            school['2학년 전채 학생 수'] = school['2학년(남)'] + school['2학년(여)']
            school['3학년 전채 학생 수'] = school['3학년(남)'] + school['3학년(여)']

            if school['1학년 전채 학생 수'] != 0 and school['2학년 전채 학생 수'] != 0 and school['3학년 전채 학생 수'] != 0:
                school['1학년 남자 비율'] = school['1학년(남)'] / school['1학년 전채 학생 수'] * 100
                school['2학년 남자 비율'] = school['2학년(남)'] / school['2학년 전채 학생 수'] * 100
                school['3학년 남자 비율'] = school['3학년(남)'] / school['3학년 전채 학생 수'] * 100

                school['1학년 여자 비율'] = school['1학년(여)'] / school['1학년 전채 학생 수'] * 100
                school['2학년 여자 비율'] = school['2학년(여)'] / school['2학년 전채 학생 수'] * 100
                school['3학년 여자 비율'] = school['3학년(여)'] / school['3학년 전채 학생 수'] * 100

            school['전채 학생 수'] = school['1학년 전채 학생 수'] + school['2학년 전채 학생 수'] + school['3학년 전채 학생 수']

            school_li.append(school)

top5_schools = sorted(school_li, key=lambda x: x['전채 학생 수'], reverse=True)[:5]
table = PrettyTable()

table.field_names = ['학교명', '전채 학생 수', '1학년 전채 학생 수', '1학년(남)', '1학년(여)', '1학년 여자 비율', '2학