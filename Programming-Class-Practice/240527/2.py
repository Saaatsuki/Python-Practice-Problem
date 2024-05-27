import random  # ランダムモジュールをインポートします。
import turtle  # turtleモジュールをインポートします。

# グラフィックウィンドウ（画面）を生成し、タイトルを設定します。
screen = turtle.Screen()
screen.title("Turtle キーボードイベント処理例")

# 亀のオブジェクトを生成します。
t = turtle.Turtle()

# ウィンドウの幅と高さを取得し、半分の値を計算します。
width = screen.window_width() // 2
height = screen.window_height() // 2

print(width, height)  # ウィンドウの幅と高さの半分を出力します。

# 亀の位置がウィンドウの境界に達したかを確認し、境界に達したら後退する関数を定義します。
def move_turtle():
    x, y = t.position()
    if x >= width or x <= -width or y >= height or y <= -height:
        t.backward(10)

# 亀を前進させ、現在の位置を出力する関数を定義します。
def move_forward():
    t.forward(10)
    move_turtle()
    x, y = t.position()
    print(x, y)

# 亀を後退させる関数を定義します。
def move_backward():
    t.backward(10)
    move_turtle()

# 亀を左に回転させる関数を定義します。
def turn_left():
    t.left(15)

# 亀を右に回転させる関数を定義します。
def turn_right():
    t.right(15)

# 亀のペンの色をランダムに変更する関数を定義します。
def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))

# 亀のペンの色を黒に変更する関数を定義します。
def change_black():
    t.pencolor("black")

# 亀のペンの色を赤に変更する関数を定義します。
def change_red():
    t.pencolor("red")

# 亀のペンの色を赤と黒の間で交互に変更する関数を定義します。
def change_red_black():
    if t.pencolor() == "red":
        t.pencolor("black")
    else:
        t.pencolor("red")

# ユーザーに色を選択させる関数を定義します。
def change_color():
    print("色選択：")
    print("1：青色")
    print("2：赤色")
    print("3：黄色")

    while True:
        input_value = int(input("数字選択："))
        if input_value == 1:
            t.pencolor("blue")
            break
        elif input_value == 2:
            t.pencolor("red")
            break
        elif input_value == 3:
            t.pencolor("yellow")
            break
        else:
            print("無効な入力です。もう一度入力してください。")

# キーボードイベントのリスニングを開始します。
screen.listen()

# 特定のキーが押されたときに関数を呼び出すイベントを設定します。
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_random, "c")
screen.onkey(change_black, "b")
screen.onkey(change_red, "r")
screen.onkey(change_red_black, "i")
screen.onkey(change_color, "t")

# turtleグラフィックウィンドウのイベントループを開始します。
screen.mainloop()
