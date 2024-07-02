li = []
for _ in range(10):
    num = int(input())
    amari = num%42
    if amari not in li:
        li.append(amari)

print(len(li))
