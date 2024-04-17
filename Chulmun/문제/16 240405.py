#　出発時刻、到着時刻、移動距離を入力
departure_hour = int(input("①Prease enter your departure hour : "))
departure_minuts = int(input("②Prease enter your departure time : "))
arrival_hour = int(input("③Prease enter your arrival hour : ")) 
arrival_minuts = int(input("④Prease enter your arrival time : ")) 
travel_distance = int(input("⑤Prease enter your travel distance : "))

def calculation_result ():
    global departure_hour
    global departure_minuts
    global arrival_hour
    global arrival_minuts
    global travel_distance
    
    # 移動時間を分単位で計算＆移動時間を時間単位に変換
    travel_minuts = ((arrival_hour*60)+arrival_minuts) - ((departure_hour*60)+departure_minuts)
    travel_hour = travel_minuts / 60
    # 平均速度
    avarage_speeed = travel_distance / travel_hour
    
    if (avarage_speeed < 60):
        msg = "slowlyy"
    elif (60 <= avarage_speeed < 90):
        msg = "usuallyyy"
    elif (90 <= avarage_speeed):
        msg = "speedyyyyyyyyy"
    
    
    print("travel distance : ",float(travel_distance),"km")
    print("departure time : ",departure_hour," : ",departure_minuts)
    print("arrival time : ",arrival_hour," : ",arrival_minuts)
    print("avarage speed : ",avarage_speeed,"km/h")
    print("speed : Your speed is",msg)


calculation_result()