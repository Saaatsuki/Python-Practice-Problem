num = int(input())

print((" "*(num-1))+"*")
if not num==1:
    for i in range(1,num):
        print((" "*((num-i-1))+"*"+(" "*(i*2-1))+"*"))