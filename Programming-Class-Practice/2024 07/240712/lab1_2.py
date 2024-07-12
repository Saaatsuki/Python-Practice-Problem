import csv

with open('2024_std_num_high_school.csv' , newline='',encoding='utf-8-sig') as f :
    reader = csv.DictReader(f)


    boy_sum_1 = 0
    boy_sum_2 = 0
    boy_sum_3 = 0
    girl_sum_1 = 0
    girl_sum_2 = 0
    girl_sum_3 = 0

    for row in reader:
        if row["제외여부"]=="N":
            boy_sum_1 += int(row['1학년(남)'])
            boy_sum_2 += int(row['2학년(남)'])
            boy_sum_3 += int(row['3학년(남)'])
            girl_sum_1 += int(row['1학년(여)'])
            girl_sum_2 += int(row['2학년(여)'])
            girl_sum_3 += int(row['3학년(여)'])

            boy_sum_all = boy_sum_1 + boy_sum_2 + boy_sum_3
            girl_sum_all = girl_sum_1 + girl_sum_2 + girl_sum_3

            sum_all = boy_sum_all + girl_sum_all

            boy_p = boy_sum_all / sum_all * 100
            girl_p = girl_sum_all / sum_all * 100

print(f"전채 고등학교 수 : {(sum_all):,} 명")
print(f"남성 고등학교 수 : {(boy_sum_all):,} 명")
print(f"여성 고등학교 수 : {(girl_sum_all):,} 명")
print(f"남성 학생 비율 : {(boy_p):.2f} %")
print(f"남성 학생 비율 : {(girl_p):.2f} %")