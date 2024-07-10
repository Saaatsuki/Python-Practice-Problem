f_handler_1 = open("text_1.txt" , "w")
f_handler_2 = open("text_2.txt" , "w")
f_handler_3 = open("text_3.txt" , "w")

f_handler_1.write("안녕하세용")
f_handler_2.write("Hello")
f_handler_3.write("こんにちは")

f_handler_1.close()
f_handler_2.close()
f_handler_3.close()