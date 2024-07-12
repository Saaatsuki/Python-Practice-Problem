import csv

def get_field_by_int(row, field_name):
    # 주어진 행의 특정 필드 이름에 대한 값을 정수로 변환합니다.
    # 값이 숫자로만 구성되어 있을 경우에만 변환하고, 그렇지 않을 경우 0을 반환합니다.
    return int(row[field_name]) if row[field_name].isdigit() else 0

file_path = "2024_std_num_high_school.csv"  # CSV 파일 경로 설정

std_num = {}  # 각 교육청별로 학년과 성별에 따른 학생 수를 저장할 딕셔너리 초기화

# 파일 열기
with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)  # csv 파일을 읽기 위한 DictReader 객체 생성
    
    # 모든 레코드를 순회
    for row in csv_reader:
        # 해당 교육청이 std_num 딕셔너리에 없으면 초기화
        if row["시도교육청"] not in std_num:
            std_num[row["시도교육청"]] = [0] * 6  # 각 학년의 남녀 학생 수를 0으로 초기화
        
        # 학년별 성별 합산을 위한 반복문
        for grade, index in enumerate(range(0, len(std_num[row["시도교육청"]]), 2), start=1):
            # 남학생 수 합산
            std_num[row["시도교육청"]][index] += get_field_by_int(row, f"{grade}학년(남)")
            # 여학생 수 합산
            std_num[row["시도교육청"]][index+1] += get_field_by_int(row, f"{grade}학년(여)")

# 각 교육청별로 결과 출력
for key, value in std_num.items():
    print(key)
    for grade, index in enumerate(range(0, len(value), 2), start=1):
        print(f"\t{grade}학년, 남학생: {value[index]}명, 여학생: {value[index + 1]}명")

# 교육청별 총학생 수를 기준으로 정렬하여 상위 5개 출력
result = sorted(std_num.items(), key=lambda item: sum(item[1]), reverse=True)[:5]

# 정렬된 결과 출력
for index, row in enumerate(result, start=1):
    print(f"{index}등 {row[0]},\t{sum(row[1]):,} 명")
