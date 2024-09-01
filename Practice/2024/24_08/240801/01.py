num = int(input())

li = list(map(int,input().split()))

max = li[0]
min = li[0]

for i in li:
    if (i <= min):
        min = i
    if (max <= i) :
        max = i

print(f"{min} {max}")