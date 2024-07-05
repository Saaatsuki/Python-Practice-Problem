li = []
for _ in range(7):
    num = int(input())
    if not num % 2 == 0:
        li.append(num)

if len(li)==0:
    print(-1)
else:
    print(sum(li))
    print(min(li))