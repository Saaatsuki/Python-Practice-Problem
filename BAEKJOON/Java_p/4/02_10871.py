num1 , num2 = map(int,input().split())

li = list(map(int,input().split()))

for i in li:
    if i < num2:
        print(i,end=" ")