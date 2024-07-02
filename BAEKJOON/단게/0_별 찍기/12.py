num = int(input())
for i in range(1,num):
    print((" "*(num-i))+("*"*i))
for i in range(num,0,-1):
    print((" "*(num-i))+("*"*i))