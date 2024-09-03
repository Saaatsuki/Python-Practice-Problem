num = int(input())

for i in range(num,0,-1):
    print(f"{' '*(num-i)}{'*'*i}{'*'*(i-1)}")