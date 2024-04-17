a,b = map(int,input().split())
print(bool(a) ^ bool(b))




a,b = map(int,input().split())
print((bool(a) and (not bool(b))) or ((not bool(a)) and bool(b)))