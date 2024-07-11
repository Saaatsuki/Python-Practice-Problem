import csv

def sort_list_max_remove(lst):
    sorted_list = []
    while lst:
        max_elem = max(lst)
        sorted_list.append(max_elem)
        lst.remove(max_elem)
    return sorted_list

with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    # 1학년(남),1학년(여),2학년(남),2학년(여),3학년(남),3학년(여)
    boy_sum_1 = 0
    girl_sum_1 = 0
    boy_sum_2 = 0
    girl_sum_2 = 0
    boy_sum_3 = 0
    girl_sum_3 = 0
    all_stu_sum_li = []


    for row in reader:
        if row["제외여부"]=="N":
            boy_sum_1 += int(row["1학년(남)"])
            girl_sum_1 += int(row["1학년(여)"])
            boy_sum_2 += int(row["2학년(남)"])
            girl_sum_2 += int(row["2학년(여)"])
            boy_sum_3 += int(row["3학년(남)"])
            girl_sum_3 += int(row["3학년(여)"])
    
        sum_1 = boy_sum_1 + girl_sum_1
        sum_2 = boy_sum_2 + girl_sum_2
        sum_3 = boy_sum_3 + girl_sum_3

        all_stu_sum = sum_1 + sum_2 + sum_3

        boy_p_1 = boy_sum_1 / sum_1 * 100
        girl_p_1 = 100 - boy_p_1

        boy_p_2 = boy_sum_2 / sum_2 * 100
        girl_p_2 = 100 - boy_p_2

        boy_p_3 = boy_sum_3 / sum_3 * 100
        girl_p_3 = 100 - boy_p_3


        print(f'{row["학교명"]}')
        print(f"\t전채 고등학교 수 : {all_stu_sum:,} 명")
        print(f"\t1학년 - 남학생 수 : {boy_sum_1:,} 명, 여학생 수 : {girl_sum_1:,} 명, {boy_p_1:.2f} %, {girl_p_1:.2f} %")
        print(f"\t2학년 - 남학생 수 : {boy_sum_2:,} 명, 여학생 수 : {girl_sum_2:,} 명, {boy_p_2:.2f} %, {girl_p_2:.2f} %")
        print(f"\t3학년 - 남학생 수 : {boy_sum_3:,} 명, 여학생 수 : {girl_sum_3:,} 명, {boy_p_3:.2f} %, {girl_p_3:.2f} %")