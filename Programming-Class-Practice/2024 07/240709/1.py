f_hander = open("test.txt" , "r+")

msg = f_hander.read()

msg += "hello world"

f_hander.write(msg)

f_hander.close()