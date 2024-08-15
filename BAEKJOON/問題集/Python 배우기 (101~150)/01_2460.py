li = []
cou = 0
for _ in range(10):
    num1 , num2 = map(int,input().split())
    cou += (num2 - num1)
    li.append(cou)

print(max(li))