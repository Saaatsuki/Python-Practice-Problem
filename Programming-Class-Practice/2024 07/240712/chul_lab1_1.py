import csv

file_path = "2024_std_num_high_school.csv"

# "시도교육청"의 중복되지 않은 값을 저장하기 위한 집합
education_office = set()

# 파일을 열고
with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    # 모든 레코드를 순회
    for row in csv_reader:
        # 중복되지 않은 "시도교육청" 필드를 집합에 추가
        education_office.add(row["시도교육청"])
    
# 중복되지 않은 "시도교육청"의 값을 출력
for index, office in enumerate(sorted(education_office), start=1):
    print(f"{index}번, {office}")
