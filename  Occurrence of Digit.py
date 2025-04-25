# Q25. Count the Occurrence of a Digit in a given Number

number = input()
digit =input()

if len(digit)==1:
    count=0
    for i in number:
        if i==digit:
            count+=1
    print(count)        
else:            
    print("enter a single digit number")        