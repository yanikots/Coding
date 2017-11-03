firstNumber = int(input("Type a number:"))
secondNumber = int(input("Type another number:"))

menu = "Would you like to:\n\
    1. Multiply these?\n\
    2. Divide the first number to the second one?\n\
    3. Add them together?\n\
    4. Subtract the second number from the first one?\n\
    5. Find out the power?\n\
    6. Square both number?\n\
    7. Find the square root of both?\n"

answer = int(input(menu))

if answer == 1:
    print (firstNumber * secondNumber)
elif answer == 2:
    print (firstNumber / secondNumber)
elif answer == 3:
    print (firstNumber + secondNumber)
elif answer == 4:
    print (firstNumber - secondNumber)
elif answer == 5:
    print (firstNumber**secondNumber)
elif answer == 6:
    print(firstNumber**2 ,"and" ,secondNumber**2)
elif answer == 7:
    print (firstNumber**.5 ,"and" ,secondNumber**.5)
