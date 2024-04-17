性別 = input("あなたの性別はなんなん：")

メッセージ = "あなたの性別は{}ですね"

if (性別 == "男"):
    print(メッセージ.format("MAN"))
elif (性別 == "女"):
    print(メッセージ.format("WOMAN"))
else:
    print(メッセージ.format("その他"))