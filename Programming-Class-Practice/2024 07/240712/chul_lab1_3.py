import csv

def get_field_by_int(row, field_name):
    # 주어진 row의 field_name을 확인하고, 숫자로만 구성된 경우 int로 변환하여 반환
    # 숫자가 아닐 경우 0 반환
    return int(row[field_name]) if row[field_name].isdigit() else 0
    
file_path = "2024_std_num_high_school.csv"  # CSV 파일의 경로

std_list = [0] * 6  # 각 학년의 남녀 학생 수를 저장할 리스트 초기화

# 파일 열기
with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)  # 파일을 읽기 위한 DictReader 객체 생성
    
    # 파일의 모든 행(row) 순회
    for row in csv_reader:
        # 각 학년의 남녀 학생 수를 순회하여 계산
        for grade, index in enumerate(range(0, len(std_list), 2), start=1):
            std_list[index] += get_field_by_int(row, f"{grade}학년(남)")  # 남학생 수 합산
            std_list[index + 1] += get_field_by_int(row, f"{grade}학년(여)")  # 여학생 수 합산
        
# 전체 학생 수 출력
print(f"전체 학생 수 : {sum(std_list):,}")

# 각 학년별 학생 수 및 비율 계산 및 출력
for grade, index in enumerate(range(0, len(std_list), 2), start=1):
    total_students = sum(std_list[index:index + 2])  # 학년별 총 학생 수 계산
    if total_students > 0:
        percentage_male = std_list[index] / total_students * 100  # 남학생 비율 계산
        percentage_female = std_list[index + 1] / total_students * 100  # 여학생 비율 계산
    else:
        percentage_male, percentage_female = 0, 0  # 학생 수가 0인 경우 비율도 0으로 설정
    print(f"{grade}학년 - 남학생 수 {std_list[index]:,}, 여학생 수 {std_list[index + 1]:,}, 남학생 비율 {percentage_male:.2f}%, 여학생 비율 {percentage_female:.2f}%")
