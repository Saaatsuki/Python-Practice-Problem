password = input("Please enter your password🔒：")

# パスワードの安全性を検証する関数
def validate_password(password):
    # 条件1：パスワードの長さが8文字以上
    length_condition = len(password) >= 8

    # 条件2：パスワードに少なくとも1つの数字が含まれている
    digit_condition = any(char.isdigit() for char in password)

    # 条件3：パスワードに少なくとも1つの大文字が含まれている
    uppercase_condition = any(char.isupper() for char in password)

    # すべての条件を満たしている場合はTrueを返す
    return length_condition and digit_condition and uppercase_condition


if validate_password(password):
    print("Your password is secure┏ (゜ω゜)=")
else:
    print("Your password is not secureヾ(•ω•`)o")