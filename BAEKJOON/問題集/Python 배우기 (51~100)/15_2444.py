num = int(input())

for i in range(num):
    print(f"{' '*(num-(i+1))}{'*'*(i+1)}{'*'*i}")
for i in range(num-2,-1,-1):
    print(f"{' '*(num-(i+1))}{'*'*(i+1)}{'*'*i}")