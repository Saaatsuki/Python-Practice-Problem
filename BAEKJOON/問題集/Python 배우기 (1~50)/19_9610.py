T = int(input())

Q1 = []
Q2 = []
Q3 = []
Q4 = []
AXIS = []

for _ in range(T):
    num1 , num2 = map(int,input().split())

    if 0 < num1 and 0 < num2:
        Q1.append(1)
    elif num1 < 0 and 0 < num2:
        Q2.append(1)
    elif num1 < 0 and num2 < 0:
        Q3.append(1)
    elif 0 < num1 and num2 < 0:
        Q4.append(1)
    else:
        AXIS.append(1)

print("Q1:",sum(Q1))
print("Q2:",sum(Q2))
print("Q3:",sum(Q3))
print("Q4:",sum(Q4))
print("AXIS:",sum(AXIS))
