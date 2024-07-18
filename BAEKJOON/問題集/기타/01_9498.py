num = int(input())

score = "A" if 90<=num else "B" if 80<=num<90 else "C" if 70<=num<80 else "D" if 60<=num<70 else "F"
print(score)