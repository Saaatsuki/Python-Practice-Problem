num = int(input)

for i in range(num):
    n1,n2 = map(int,input().split())
    print(f"Case #{i+1}: {n1} + {n2} = {n1+n2}")
