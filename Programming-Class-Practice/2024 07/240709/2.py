import os

msg = os.getcwd()
print(type(msg) , msg)

msg = os.listdir()
print(type(msg) , msg)

# フォルダをつくる
os.mkdir("kin")

# 今作業しているディレクトリを変更
os.chdir("kin")

msg = os.getcwd()
print(type(msg) , msg)