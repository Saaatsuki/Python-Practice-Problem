hour1 , minu1 , time1 = map(int,input().split(":"))

hour2 , minu2 , time2 = map(int,input().split(":"))

res = (hour2 * 3600 + minu2 * 60 + time2) - (hour1 * 3600 + minu1 * 60 + time1)

if res<0:
    res += 60 * 60 * 24

res_hour = res // 3600
res_minu = (res%3600) // 60
res_time = res%60

print(f"{res_hour:02d}:{res_minu:02d}:{res_time:02d}")