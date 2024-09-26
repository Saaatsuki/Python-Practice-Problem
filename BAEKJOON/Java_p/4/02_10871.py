num1 , num2 = map(int,input().split())

li = list(map(int,input().split()))

li2 = []
for i in li:
    if i < 5:
        print(i,end=" ")