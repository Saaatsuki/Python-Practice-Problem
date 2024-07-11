import csv

with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    # 1학년(남),1학년(여),2학년(남),2학년(여),3학년(남),3학년(여)
    all_boy_sum = 0
    all_girl_sum = 0
    for row in reader:

        for i in range(1, 4):
            if row["제외여부"]=="N":
                all_boy_sum += int(row[f"{i}학년(남)"])
                all_girl_sum += int(row[f"{i}학년(여)"])
    all_stu_sum = all_boy_sum + all_girl_sum
    all_boy_p = all_boy_sum / all_stu_sum * 100
    all_girl_p = 100 - all_boy_p

    print(f"전채 고등학교 수 : {all_stu_sum:,} 명")
    print(f"님자 고등학교 수 : {all_boy_sum:,} 명")
    print(f"여자 고등학교 수 : {all_girl_sum:,} 명")
    print(f"남성 학생 비율 : {all_boy_p:.2f} %")
    print(f"여성 학생 비율 : {all_girl_p:.2f} %")