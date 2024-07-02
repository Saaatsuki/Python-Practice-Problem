hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))
timer = int(input("Enter the time after which the alarm will ring (in minutes): "))

# 時間と分を分の総数に変換
total_minutes = hour * 60 + minute

# 指定された時間後の合計分数を計算
alarm_time = total_minutes + timer

# 24時間制に変換
alarm_hour = alarm_time // 60
alarm_minute = alarm_time % 60

# 時間が24を超える場合は調整
alarm_hour %= 24

print("Alarm set for:", "{:02d}:{:02d}".format(alarm_hour, alarm_minute))
