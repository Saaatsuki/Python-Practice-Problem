li = []
for i in range(10):
    num = int(input())
    nam = num % 42
    if not nam in li:
        li.append(nam)

print(len(li))