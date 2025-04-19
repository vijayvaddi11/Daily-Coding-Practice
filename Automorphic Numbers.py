# Q.Find It's an Automorphic Number or Not

str_num = input()
number=int(str_num)
square_num =str(number**2)
print("It's an Automorphic Number") if int(square_num[-len(str_num):])==number else print("It's not an Automorphic Number")