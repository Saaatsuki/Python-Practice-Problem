def printName(family,name):
    print(f"{family} {name} 님 안녕하세요")
# printName("카와이")  
# printName("사츠키")

name_li = ["아야","사츠키","토모타카"]
for i in name_li:
    printName("카와이",i)


def sumavg(avgLIst):
    num_li_sum = 0
    [num_li_sum:=num_li_sum+ i for i in avgLIst]
    num_avg = num_li_sum / len(avgLIst)
    print(f"合計：{num_li_sum} 　平均：{num_avg}")

num_li =[]
for i in range(3):
    input_num = int(input(f"{i+1}번째 깂을 입력해!! : "))
    num_li.append(input_num)

sumavg(num_li)



