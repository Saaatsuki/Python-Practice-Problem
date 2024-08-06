num1 , num2 , num3 = map(int,input().split())

num_li = [num1 , num2 , num3]

num_li.remove(max(num_li))
print(max(num_li))