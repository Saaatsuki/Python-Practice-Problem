while True:
    hour = int(input("시간을 입력해주세요 : "))
    minute = int(input("분을 입력 해주세요 : "))

    if (minute>=45):
        print(hour,":",minute-45)
        break
    elif (minute<45):
        print(hour,":",60+minute-45)
        break
    else:
        print("디시 입력 해주세요")
