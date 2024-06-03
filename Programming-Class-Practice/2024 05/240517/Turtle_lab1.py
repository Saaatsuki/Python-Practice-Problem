import turtle  # turtleモジュールをインポートします。

# グラフィックウィンドウ（画面）を生成します。
screen = turtle.Screen()

# 亀のオブジェクトを生成します。
t = turtle.Turtle()

# 2回ループして長方形を描きます。
for _ in range(2):
    # 亀を前方に100ピクセル進ませます。
    t.forward(100)
    # 亀を右に90度回転させます。
    t.right(90)
    # 亀を前方に50ピクセル進ませます。
    t.forward(50)
    # 亀を右に90度回転させます。
    t.right(90)

# turtleグラフィックウィンドウが閉じられるのを防ぎます。
turtle.done()
