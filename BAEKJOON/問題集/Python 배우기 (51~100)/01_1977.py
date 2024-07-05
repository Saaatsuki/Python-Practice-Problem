num1 = int(input())
num2 = int(input())

li1 = [num**2 for num in range(1,101)]
li2 = []

for num in li1:
    if num1<=num<=num2:
        li2.append(num)
if len(li2):
    print(sum(li2))
    print(min(li2))
else:
    print(-1)