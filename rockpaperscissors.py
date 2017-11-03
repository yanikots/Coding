import random
import sys
import time
score = 0
possibility = ["rock","paper","scissors"] #all possible outcomes
replay="y" #variable to close the loop
print ("It's rock, paper, scissors with points!\nGood luck!")
while replay == "y":
    computerchoice = random.choice(possibility) #computer choosing a random outcome
    playerchoice = input("rock, paper, or scissors?") #player chooses an option
    if playerchoice == "rock":
        if computerchoice == "rock":            
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nIt's a draw!")
            score = score
            print ("Score:",score)
        elif computerchoice == "paper":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nNever lucky.")
            score = score-1
            print("Score:",score)
        elif computerchoice == "scissors":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nWow lucky you!")
            score = score+1
            print("Score:",score)
    elif playerchoice == "paper":
        if computerchoice == "rock":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nWow lucky you!")
            score = score+1
            print("Score:",score)
        elif computerchoice == "paper":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nIt's a draw!")
            score = score
            print("Score:",score)
        elif computerchoice == "scissors":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nNever lucky.")
            score = score-1
            print("Score:",score)
    elif playerchoice == "scissors":
        if computerchoice == "rock":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nNever lucky.")
            score = score-1
            print("Score:",score)
        elif computerchoice == "paper":
            print ("Computer chose...")
            print ("Wow lucky you!")
            score = score+1
            print("Score:",score)
        elif computerchoice == "scissors":
            print ("Computer chose...")
            time.sleep(1)
            print (computerchoice,"\nIt's a draw!.")
            score = score
            print("Score:",score)
    else:
        print("You need to type either rock, paper or scissors (all lowercase)") #if something goes wrong
    replay = input("Do you want to play again? y/n") #asking again and closing the loop
print ("Total score:",score)
sys.exit() #exiting the program
