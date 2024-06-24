go_ho = int(input("출발 시(시간)을 입력하세요 : "))
go_ti = int(input("출발 시(분)을 입력하세요 : "))
arr_ho = int(input("도착 시(시간)을 입력하세요 : "))
arr_ti = int(input("도착 시(분)을 입력하세요 : "))
dis = int(input("이동 거리(km)를 입력하세요 : "))

dis_ti = arr_ti - go_ti if arr_ti>=go_ti else (60 - go_ti) + arr_ti
dis_hour = arr_ho - go_ho
dis_ti_sum = dis_hour*60 + dis_ti
dis_ho_sum = dis_ti_sum / 60
speed = dis / dis_ho_sum
msg = "느림" if speed<60 else "보통" if 60<=speed<90 else "빠름"

print(f"이동 거리 : {dis:.1f}km\n출발 시간 : {go_ho}시 {go_ti}분\n도착 시간 : {arr_ho}시 {arr_ti}분\n평균 속도 : {speed:.2f}km/h\n속도 상태 : {msg}")