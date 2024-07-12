import csv

with open('2024_std_num_high_school.csv' , newline='' , encoding='utf-8-sig') as f :
    reader = csv.DictReader(f)

    boy_sum = 0
    girl_sum = 0
    boy_sum_all_li = []
    girl_sum_all_li = []
    all_sum_li = []

    for row in reader:
        if row["제외여부"]=="N":
            for i in range(1,4):
                boy_sum += int(row[f"{i}학년(남)"])
                boy_sum_all_li.append(boy_sum)

                girl_sum += int(row[f"{i}학년(여)"])
                girl_sum_all_li.append(girl_sum)

                all_sum = boy_sum + girl_sum
                all_sum_li.append(all_sum)

                boy_p = boy_sum / all_sum * 100
                girl_p = girl_sum / all_sum * 100

                if i == 1:
                    boy_sum_all = sum(boy_sum_all_li)
                    girl_sum_all = sum(girl_sum_all_li)
                    all_sum = sum(all_sum_li)

                    all_boy_p = boy_sum_all / all_sum * 100
                    all_girl_p = girl_sum_all / all_sum *100
                    print()
                    print(f"전채 고등학생 수 : {(all_sum):,} 명, 남학생 수 : {(boy_sum_all):,} 명, 여학생 수 : {(girl_sum_all)} 명, 남학생 비율 : {(all_boy_p):.2f} % , 여학생 비율 : {(all_girl_p):.2f} %")
                
                print(f"{i}학년 - 남학생 수 : {(boy_sum):,} 명, 여학생 수 : {(girl_sum):,} 명, 남학생 비율 : {(boy_p):.2f} % , 여학생 비율 : {(girl_p):.2f} %")

