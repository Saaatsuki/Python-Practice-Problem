test = int(input("시험 점수를 입력 해주세요 : "))

if (90 <= test <=100):
    print("A")
elif(80 <= test < 90):
    print("B")
elif(70 <= test < 80):
    print("C")
elif(60 <= test < 70):
    print("D")
else:
    print("F")