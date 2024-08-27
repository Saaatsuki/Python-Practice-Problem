num = int(input())

for i in range(1,6):
    print(f"{' '*(num+1-i)}{'*'*i}{'*'*(i-1)}")
for i in range(6,0,-1):
    print(f"{' '*(num+1-i)}{'*'*i}{'*'*(i-1)}")