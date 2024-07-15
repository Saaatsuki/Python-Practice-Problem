import csv


with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f :
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
            girl_sum_3 = int(row['3학년(여)'])

    boy_sum_all = boy_sum_1 + boy_sum_2 + boy_sum_3
    girl_sum_all = girl_sum_1 + girl_sum_2 + girl_sum_3
    all_sum = boy_sum_all + girl_sum_all

    all_sum_1 = boy_sum_1 + girl_sum_1
    all_sum_2 = boy_sum_2 + girl_sum_2
    all_sum_3 = boy_sum_3 + girl_sum_3

    boy_p_1 = boy_sum_1 / all_sum_1 * 100
    boy_p_2 = boy_sum_2 / all_sum_2 * 100
    boy_p_3 = boy_sum_3 / all_sum_3 * 100
    girl_p_1 = girl_sum_1 / all_sum_1 * 100
    girl_p_2 = girl_sum_2 / all_sum_2 * 100
    girl_p_3 = girl_sum_3 / all_sum_3 * 100
 
    boy_p = boy_sum_all / all_sum * 100
    girl_p = girl_sum_all / all_sum * 100

    print(f"전채 고등학생 수 : {(all_sum):,} 명, 남학생 수 : {(boy_sum_all):,} 명, 여학생 수 : {(girl_sum_all)} 명, 남학생 비율 : {(boy_p):.2f} % , 여학생 비율 : {(girl_p):.2f} %")
    print(f"1학년 - 남학생 수 : {(boy_sum_1):,} 명, 여학생 수 : {(girl_sum_1):,} 명, 남학생 비율 : {(boy_p_1):.2f} % , 여학생 비율 : {(girl_p_1):.2f} %")
    print(f"2학년 - 남학생 수 : {(boy_sum_2):,} 명, 여학생 수 : {(girl_sum_2):,} 명, 남학생 비율 : {(boy_p_2):.2f} % , 여학생 비율 : {(girl_p_2):.2f} %")
    print(f"3학년 - 남학생 수 : {(boy_sum_3):,} 명, 여학생 수 : {(girl_sum_3):,} 명, 남학생 비율 : {(boy_p_3):.2f} % , 여학생 비율 : {(girl_p_3):.2f} %")
