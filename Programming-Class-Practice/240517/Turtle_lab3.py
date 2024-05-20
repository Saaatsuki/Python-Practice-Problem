import turtle  # turtleモジュールをインポートします。

# グラフィックウィンドウ（画面）を生成します。
screen = turtle.Screen()

# 亀のオブジェクトを生成します。
t = turtle.Turtle()

# 亀に半径50ピクセルの円を描かせます。
t.circle(50)

# turtleグラフィックウィンドウが閉じられるのを防ぎます。
turtle.done()
