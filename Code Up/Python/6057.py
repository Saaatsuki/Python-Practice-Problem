a,b = map(int,input().split())
print(bool(a) == bool(b))


a,b = map(int,input().split())
if(bool(a) ^ bool(b) == True ):
    print("False")
else:
    print("True")