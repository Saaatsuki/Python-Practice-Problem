sum_li = []
for _ in range(5):
    num1,num2,num3,num4 = map(int,input().split())
    num_li = [num1,num2,num3,num4]
    num_li_sum = sum(num_li)
    sum_li.append(num_li_sum)
idx = sum_li.index(max(sum_li))
print(f"{idx+1} {max(sum_li)}")