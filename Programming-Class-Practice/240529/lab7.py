number = 5

for i in range(1,number):
    print(" "*(number-i)+"*"*(2*i-1))
for i in range(number,0,-1):
    print(" "*(number-i)+"*"*(2*i-1))

# スペースの数　：　number-1
# 星の数　：　2×i-1