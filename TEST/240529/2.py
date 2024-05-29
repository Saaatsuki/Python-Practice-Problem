# 색을 입력받아서 빨강색이면 ford 회색이면 벤틀리 검정색이면 현대 출력

color = input("put on the color : ").upper()

car = ""

#1)
if color == "RED":
    car = "ford"
elif color == "BLACK":
    car = "hyundai"
elif color == "GRAY":
    car = "bentley"

#2)
if color == "RED":
    car = "ford"
elif color == "BLACK":
    car = "hyundai"
else: 
    car = "bentley"
    
#3)
if color == "RED":
    car = "ford"
elif color == "GRAY":
    car = "bentley" 
elif color == "BLACK" or color == "BLUE":
    car = "hyundai"



print(car)