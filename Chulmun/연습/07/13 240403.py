def bar():
    # msg1 に "<< " とグローバル変数 name の値を組み合わせた文字列を代入します
    msg1 = "<< " + name
    
    # foo 関数を呼び出し、msg1 を引数として渡します
    msg2 = foo(msg1)
    # foo 関数の戻り値に空白を追加します
    msg2 += " "
    
    # pos 関数を呼び出し、msg2 を引数として渡します
    msg3 = pos(msg2)
    # pos 関数の戻り値に空白を追加します
    msg3 += " "
    # msg3 を返します
    return msg3

# foo 関数の定義
def foo(argFoo):
    # argFoo に "님" を追加した文字列を返します
    msg = argFoo + "님"
    return msg

# pos 関数の定義
def pos(argPos):
    # argPos に "안녕하세요" を追加した文字列を返します
    msg = argPos + "안녕하세요"
    return msg

# グローバル変数 name に "황예지" を代入します
name = "황예지"

# bar 関数を呼び出し、その戻り値を result 変数に代入します
result = bar()
# result を出力します
print(result)
