star = int(input())

for i in range(1,star+1):
    print(f"{' '*(i-1)}{'*'*(star-(i-1))}{'*'*((star-1)-(i-1))}")
for i in range(2,star+1):
    print(f"{' '*(star-i)}{'*'*i}{'*'*(i-1)}")