people = 0
li = []
for _ in range(4):
    num1 , num2 = map(int,input().split())
    people -= num1
    people += num2
    li.append(people)
print(max(li))