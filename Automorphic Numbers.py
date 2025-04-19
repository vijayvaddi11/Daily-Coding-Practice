# Q1.Find It's an Automorphic Number or Not

str_num = input()
number=int(str_num)
square_num =str(number**2)
if int(square_num[-len(str_num):])==number:
  print("It's an Automorphic Number") 
else:
  print("It's not an Automorphic Number")