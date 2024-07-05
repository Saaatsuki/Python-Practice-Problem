f_handler = open("test.txt" , "r+")

msg = f_handler.read()

msg += "hello world"

f_handler.write(msg)

f_handler.close()