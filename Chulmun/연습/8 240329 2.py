password = input("Please enter your password🔒：")

# パスワードの安全性を検証する関数
def validate_password(password):
    # 条件1：パスワードの長さが8文字以上
    if len(password) < 8:
        return False

    # 条件2：パスワードに少なくとも1つの数字が含まれている
    if not any(char.isdigit() for char in password):
        return False

    # 条件3：パスワードに少なくとも1つの大文字が含まれている
    if not any(char.isupper() for char in password):
        return False

    # すべての条件を満たしている場合はTrueを返す
    return True


if validate_password(password):
    print("Your password is secure┏ (゜ω゜)=")
else:
    print("Your password is not secureヾ(•ω•`)o")