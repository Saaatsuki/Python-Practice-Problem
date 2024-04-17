#クラスの中で扱う関数を【メソッド】という
class Person:
    def __init__(self,name,nationality,age):
        self.name = name
        self.nationality = nationality
        self.age = age
    

        
HwangYeji = Person("Yeji","Korea","24")

print(HwangYeji.name)
print(HwangYeji.nationality)
print(HwangYeji.age)

hashimotokanna = Person("橋本環奈","日本","25")
print(hashimotokanna.name)
print(hashimotokanna.age)

