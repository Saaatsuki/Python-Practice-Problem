import csv

file_path = "2024_std_num_high_school.csv"

std_num_male = 0    # 전체 남학생 수
std_num_female = 0  # 전체 여학생 수

# 파일 열기
with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    # 레코드 순회
    for row in csv_reader:
        # 모든 학년 학생 수 합산 : 남자
        std_num_male += int(row["계(남)"]) if row["계(남)"].isdigit() else 0
        
        # 모든 학년 학생 수 합산 : 여자
        std_num_female += int(row["계(여)"]) if row["계(여)"].isdigit() else 0
        
# 전체 학생 수 계산 : 남자 + 여자
total_std_num = std_num_male + std_num_female

if total_std_num > 0:
    # 남자 % 계산 : 남자 / 전체 학생 수 * 100
    percentage_male = std_num_male / total_std_num * 100

    # 여자 % 계산 : 여자 / 전체 학생 수 * 100
    percentage_female = std_num_female / total_std_num * 100
else:
    percentage_male = percentage_female = 0

# 결과 값 출력
print(f"전체고등학생 수 : {total_std_num:,} 명")
print(f"남학생 수 : {std_num_male:,} 명")
print(f"여학생 수 : {std_num_female:,} 명")
print(f"남학생 비율 : {percentage_male:.2f} %")
print(f"여학생 비율 : {percentage_female:.2f} %")
