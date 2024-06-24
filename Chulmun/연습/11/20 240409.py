import random

def generate_password(length):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = str(uppercase_letters.lower())
    digits = "0123456789"
    all_characters = uppercase_letters + lowercase_letters + digits
    
    # 必ず1つの大文字、1つの小文字、1つの数字を含むパスワードを生成
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits)
    
    # 残りの文字をランダムに生成し、パスワードに追加
    # lengthは生成されるパスワードの長さを表す
    # length - 3は最初の3文字（必ず1つの大文字、1つの小文字、1つの数字）を除いた
    # 残りの文字数を示す
    # for _ in range(length - 3)は残りの文字数に応じて繰り返し処理を行う
    for _ in range(length - 3):
        password += random.choice(all_characters)
        
        
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

# ユーザーが長さを入力
length = int(input("Enter the length of the password : "))

print("Generated Password : ",generate_password(length))