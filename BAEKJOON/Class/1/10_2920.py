# num1,num2,num3,num4,num5,num6,num7,num8 = map(int,input().split())

txt = input()

if txt == "1 2 3 4 5 6 7 8":
    print("ascending")
elif txt == "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")