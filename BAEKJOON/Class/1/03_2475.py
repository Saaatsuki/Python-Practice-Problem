num1,num2,num3,num4,num5 = map(int,input().split())
li = [num1,num2,num3,num4,num5]

w_num_sum = 0
for num in li:
    w_num = num ** 2
    w_num_sum += w_num

print(w_num_sum % 10)