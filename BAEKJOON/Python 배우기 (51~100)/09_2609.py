num1,num2 = map(int,input().split())

def gcd(num1, num2):
    '''gcd 関数は2つの引数 num1 と num2 を受け取ります。
        while num2 > 0: ループが続く間、num1 と num2 の値を更新します。
        num1 には num2 の値を代入し、
        num2 には num1 % num2 の結果を代入します。
        これは、num1 を num2 で割った余りを num2 に代入することを意味します。
        ループが終了したとき、num1 にはGCDの値が格納されているため、それを返します。'''
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    '''lcm 関数も2つの引数 num1 と num2 を受け取ります。
        LCMは、2つの数の積をそのGCDで割ることで求められます。
        num1 * num2 // gcd(num1, num2) は、num1 と num2 の積を、
        先ほど定義した gcd 関数を用いて求めたGCDで割った結果を返します。'''
    return num1 * num2 // gcd(num1, num2)


print(gcd(num1, num2))
print(lcm(num1, num2))