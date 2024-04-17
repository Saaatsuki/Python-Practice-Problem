num1 , num2 = map(int, input("Please enter two integers☆*: .｡. o(≧▽≦)o .｡.:*☆ : ").split())

odd_even_num1 = "even" if num1%2==0 else "odd"
odd_even_num2 = "even" if num2%2==0 else "odd"
odd_even_answer = "even" if (num1 + num2) else "odd"

print(f"{odd_even_num1}+{odd_even_num2}={odd_even_answer}")