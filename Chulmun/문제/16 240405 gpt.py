def calculation_result(departure_hour, departure_time, arrival_hour, arrival_time, travel_distance):
    departure_minutes = departure_hour * 60 + departure_time
    arrival_minutes = arrival_hour * 60 + arrival_time
    travel_time_minutes = arrival_minutes - departure_minutes

    travel_time_hours = travel_time_minutes / 60
    average_speed = travel_distance / travel_time_hours

    if average_speed < 60:
        speed_status = "遅い"
    elif 60 <= average_speed < 90:
        speed_status = "普通"
    else:
        speed_status = "速い"

    print("移動距離:", travel_distance, "km")
    print("出発時間:", departure_hour, ":", departure_time)
    print("到着時間:", arrival_hour, ":", arrival_time)
    print("平均速度:", average_speed, "km/h")
    print("速度状態:", speed_status)

departure_hour = int(input("出発時間の時を入力してください: "))
departure_time = int(input("出発時間の分を入力してください: "))
arrival_hour = int(input("到着時間の時を入力してください: ")) 
arrival_time = int(input("到着時間の分を入力してください: ")) 
travel_distance = int(input("移動距離を入力してください: "))

calculation_result(departure_hour, departure_time, arrival_hour, arrival_time, travel_distance)
