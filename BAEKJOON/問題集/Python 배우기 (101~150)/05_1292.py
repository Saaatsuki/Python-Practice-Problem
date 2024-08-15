num1 , num2 = map(int,input().split())

li = []

for i in range(1,num2):
    for _ in range(i):
        li.append(i)

print(sum(li[num1-1:num2]))

