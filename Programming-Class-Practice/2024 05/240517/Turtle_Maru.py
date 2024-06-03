import turtle

# 初期設定
screen = turtle.Screen()
screen.setup(width=600, height=600)
t = turtle.Turtle()

# 円を描画していくループ
radius = 200
while radius > 0:
    t.circle(radius)
    radius -= 10  # 円の半径を10ずつ減らす

# 終了処理
screen.mainloop()
