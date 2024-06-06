goout_hour = int(input("출발 시(시간)을 입력하세요 : "))
goout_minu = int(input("출발 시(분)을 입력하세요 : "))
arr_hour = int(input("도착 시(시간)을 입력하세요 : "))
arr_minu = int(input("출발 시(분)을 입력하세요 : "))
move_km = int(input("이동 거리 : "))

move_hour = arr_hour - goout_hour
move_minu = arr_minu - goout_minu if arr_minu>=goout_minu else (60-goout_minu)+arr_minu
move_minu_sum = move_hour*60 + move_minu
move_hour_sum = move_minu_sum/60
avg_speed = move_km / move_hour_sum
msg = "빠름" if 90<=avg_speed else "보통" if 60<=avg_speed<90 else "느림" 

print(f"이동 거리 : {move_km:.1f}\n출발 시간 : {goout_hour}시 {goout_minu}분\n도착 시간 : {arr_hour}시 {arr_minu}분\n평균 속도 : {avg_speed:.2f}km/h\n속도 상태 : {msg}")
