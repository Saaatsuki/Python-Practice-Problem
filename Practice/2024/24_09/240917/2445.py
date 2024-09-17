num = int(input())

for i in range(1,num+1):
    print(f"{'*'*i}{' '*((num-i)*2)}{'*'*i}")
for i in range(num-1,0,-1):
    print(f"{'*'*i}{' '*((num-i)*2)}{'*'*i}")