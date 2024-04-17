# bar関数の定義
def bar(argInputBar):
    # メッセージの初期化
    msg = "Hello!!!"
    # foo関数を呼び出して得られたメッセージを現在のメッセージに追加
    msg = msg + foo(argInputBar)
    # 出力用のメッセージを返す
    return msg
    
# foo関数の定義
def foo(argInputFoo):
    # 引数に "様" を追加してメッセージを生成
    msg = argInputFoo + "様"
    # 生成したメッセージを返す
    return msg

# bar関数を使ってメッセージを生成
MyMsg = bar("Kawai Satsuki")


# 生成されたメッセージを出力
print(MyMsg)