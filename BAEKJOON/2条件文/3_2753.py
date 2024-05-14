leap_year = int(input("정수를 입력해주세요 : "))

if ((leap_year%4==0 and leap_year%100!=0) or ( leap_year%400==0)):
    print("leap year")
else:
    print("not leap year")