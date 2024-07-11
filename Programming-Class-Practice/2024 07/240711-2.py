import csv
from prettytable import PrettyTable

# CSV 파일 경로
csv_file_path = 'your_file_path.csv'  # 적절한 파일 경로로 변경

# 데이터를 읽어들임
schools = []

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        school = {
            '학교명': row['학교명'],
            '1학년 남학생': int(row['1학년 남학생']),
            '1학년 여학생': int(row['1학년 여학생']),
            '2학년 남학생': int(row['2학년 남학생']),
            '2학년 여학생': int(row['2학년 여학생']),
            '3학년 남학생': int(row['3학년 남학생']),
            '3학년 여학생': int(row['3학년 여학생'])
        }
        school['전체 학생 수'] = school['1학년 남학생'] + school['1학년 여학생'] + school['2학년 남학생'] + school['2학년 여학생'] + school['3학년 남학생'] + school['3학년 여학생']
        school['남학생 합계'] = school['1학년 남학생'] + school['2학년 남학생'] + school['3학년 남학생']
        school['여학생 합계'] = school['1학년 여학생'] + school['2학년 여학생'] + school['3학년 여학생']
        school['남녀 비율'] = school['남학생 합계'] / school['여학생 합계'] if school['여학생 합계'] > 0 else float('inf')
        schools.append(school)

# 전체 학생 수로 정렬하여 상위 5개 학교를 추출
top5_schools = sorted(schools, key=lambda x: x['전체 학생 수'], reverse=True)[:5]

# PrettyTable 설정
table = PrettyTable()
table.field_names = ["학교명", "전체 학생 수", "1학년 남학생", "1학년 여학생", "2학년 남학생", "2학년 여학생", "3학년 남학생", "3학년 여학생", "남학생 합계", "여학생 합계", "남녀 비율"]

# 상위 5개 학교의 정보를 테이블에 추가
for school in top5_schools:
    table.add_row([
        school['학교명'],
        school['전체 학생 수'],
        school['1학년 남학생'], school['1학년 여학생'],
        school['2학년 남학생'], school['2학년 여학생'],
        school['3학년 남학생'], school['3학년 여학생'],
        school['남학생 합계'], school['여학생 합계'],
        f"{school['남녀 비율']:.2f}"
    ])

# 테이블 출력
print(table)