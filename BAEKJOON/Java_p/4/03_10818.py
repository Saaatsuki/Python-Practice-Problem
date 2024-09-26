num = int(input())

li = list(map(int,input().split()))

li_max = li[0]

for i in range(len(li)):
    if li[i] > li_max:
        li_max = li[i]

print(li_max)
