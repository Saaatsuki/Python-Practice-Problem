hour, minute = map(int, input().split())

if minute >= 45:
    new_minute = minute - 45
    new_hour = hour
else:
    new_minute = 60 + minute - 45
    new_hour = hour - 1 if hour > 0 else 23

print(f"{new_hour} {new_minute}")
