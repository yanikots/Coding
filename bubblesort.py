re = "yes"
while re == "yes":
    numbers = []
    n = int(input("Enter how many elements you want in your sort: "))
    for i in range(0, n):
        x = int(input("Enter the number you want to add to the array: "))
        numbers.append(x)
    changes = True
    while changes==True:
        changes = False
        for i in range (0,len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers [i+1]
                numbers[i+1] = temp
                changes = True
    print (numbers)
    re = input("Do you want do it again? yes/no?")
