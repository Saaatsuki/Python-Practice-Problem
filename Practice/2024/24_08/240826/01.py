num = int(input())

li = list(map(int,input().split()))

sum = sum(li)
avg = sum / len(li)

print(f"{avg:.2f}")