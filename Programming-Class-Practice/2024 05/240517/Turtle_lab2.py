import turtle  # turtleモジュールをインポートします。

# グラフィックウィンドウ（画面）を生成します。
screen = turtle.Screen()

# 亀のオブジェクトを生成します。
t = turtle.Turtle()

# 3回ループして正三角形を描きます。
for _ in range(3):
    # 亀を前方に100ピクセル進ませます。
    t.forward(100)
    # 亀を左に120度回転させます。
    # 正三角形の内角は60度ですが、外角は120度になります。
    t.left(120)
    
# turtleグラフィックウィンドウが閉じられるのを防ぎます。
turtle.done()
