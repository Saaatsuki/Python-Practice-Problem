while True:
    word = input()
    if word == "END":
        break
    else:
        word_li = list(word)
        word_li = word_li[::-1]
        print("".join(word_li))