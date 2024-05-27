import random
import turtle

screen = turtle.Screen()
screen.title("Turtle 기보드 이벤트 처리 예제")

t = turtle.Turtle()

def move_forward():
    t.forward(100)
    
    x , y = t.position()
    print(x,y)
    
def move_backward():
    t.backward(100)
    
def turn_left():
    t.left(15)

def turn_right():
    t.right(15)
    
def move_random():
    colors = ["red","green","blue","yellow","purple","orange"]
    t.pencolor(random.choice(colors))

def change_black():
    t.pencolor("Black") 
    
def change_Red():
    t.pencolor("Red")
    
def change_red_black():
    if t.pencolor() == "red":
        t.pencolor("black")
    elif t.pencolor() == "black":
        t.pencolor("red")
        
# def change_color():
#     while not (1 <= input <= 3):
#         print("色選択：")
#         print("1：青色")
#         print("2：赤色")
#         print("3：黄色")
#         input_value = int(input("数字選択："))
        
    print("色選択：")
    print("1：青色")
    print("2：赤色")
    print("3：黄色")

    while True:
        input_value = int(input("数字選択："))
        # if 1 <= input_value <= 3:
        #     break
        
        if input_value == 1:
            t.pencolor("blue")
            break
        elif input_value == 2:
            t.pencolor("red") 
            break
        elif input_value == 3:
            t.pencolor("yellow")  
            break
        # else:
        #     continue




    
  
        
           
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(move_random,"c")
screen.onkey(change_black,"b")
screen.onkey(change_Red,"r")
screen.onkey(change_red_black,"i")
screen.onkey(change_color,"t")

screen.mainloop()