import random
import turtle

screen = turtle.Screen()
screen.title("Turtle 기보드 이벤트 처리 예제")

t = turtle.Turtle()

def move_forward():
    t.forward(10)
    
def move_backward():
    t.backward(10)
    
def turn_left():
    t.left(15)

def turn_right():
    t.right(15)
    
def move_random():
    colors = ["red","green","blue","yellow","purple","orange"]
    t.pencolor(random.choice(colors))

def change_black():
    t.pencolor("Black") 
    
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(move_random,"c")
screen.onkey(change_black,"b")

screen.mainloop()