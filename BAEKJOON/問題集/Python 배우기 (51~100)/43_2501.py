num1 , num2 = map(int,input().split())

li = []
for num in range(1,num1+1):
    N = num1 % num
    if N == 0:
        li.append(num)

