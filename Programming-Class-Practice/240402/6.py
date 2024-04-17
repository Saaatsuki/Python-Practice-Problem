def foo():
    msg = "Hello"
    
    def bar():
        nonlocal msg
        print(msg)