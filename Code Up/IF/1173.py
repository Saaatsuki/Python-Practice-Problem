hour,time = map(int,input("Please enter the hour and time : ").split())

if (time >= 30):
    three_minutes_ago = (hour,time-30)
elif(time < 30):
    three_minutes_ago = (hour-1,60+time-30)

print(three_minutes_ago)