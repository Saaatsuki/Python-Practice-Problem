num = int(input())

for i in range(num , 0 , -1) :
    print(f"{' '*(num-i)}{'*'*i}{'*'*(i-1)}")
for i in range(2 , num+1) :
    print(f"{' '*(num-i)}{'*'*i}{'*'*(i-1)}")    