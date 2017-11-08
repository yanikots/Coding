import random
print ("Hello, can you guess my number?\nIt's between 1 and 100.\nIf your guess is lower than my number, I will say it is lower,\nIf it's higher I will say it is higher.\nGood Luck!")
replay = "y"
while replay == "y":
    number = random.randint(1,101)
    guessCount = 0
    found = False
    while not found:
        guess = int(input("What is your guess?"))
        guessCount = guessCount+1
        if guess == number:
            print ("Wow you found my number!")
            print ("Number of guesses:",guessCount)
            found = True
        elif guess > number:
            print ("Go lower!")
            print ("Number of guesses:",guessCount)
        elif guess < number:
            print ("Go higher!")
            print ("Number of guesses:",guessCount)
    replay = input("Do you want to play again? y/n")

        

