def sum_num(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    result = 0
    return result

num_li = [int(input(f"{i+1}번째의 숫자를 입력하세요 : ")) for i in range(10)]
sum_num(*num_li)
num1,num2,num3,num4,num5,num6,num7,num8,num9,num10 = num_li
num_li_sum = 0
[num_li_sum:=num_li_sum + i for i in num_li]
print(num_li_sum)
