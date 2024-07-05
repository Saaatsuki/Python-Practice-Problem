con = int(input())

li1 = list(map(int,input().split()))
li2 = []
plus = 1
for num in li1:
    if num==1:
        li2.append(plus)
        plus += 1
    else:
        plus = 1

print(sum(li2))