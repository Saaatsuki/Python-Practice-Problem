li = list(map(int,input().split()))

max_value  = li[0]
idx = -1

for i in range(len(li)):
    if (max_value <= li[i]):
        max_value = li[i]
        idx = i

print(max)
print(idx)