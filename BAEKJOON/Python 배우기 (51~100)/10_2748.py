num = int(input())

li = [0,1,1]
for i in range(3,num+1):
    li.append(li[i-2]+li[i-1])

print(li[num])