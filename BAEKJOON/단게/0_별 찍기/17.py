num = int(input())
print(" "*(num-1)+"*")
if not num==1:
    for i in range(1,num-1):
        print(f"{' '*(num-1-i)}*{' '*(i*2-1)}*")
print(f"{'*'*(num*2-1)}")