import random
#create a notepad file called 'Wordlist'
#then copy a random long text from the internet (e.g. wikipedia sport)
#the program will choose a random suitable word from there and the game will start

def extractwords(filename, number):
    myfile=open(filename+".txt", "r")
    details=myfile.readlines()
    myfile.close()
    words=[]
    for i in details:
        for item in i.split():
            letter=True
            for j in item:
                if j.isalpha() == False:
                    letter=False
            item = item.lower()
            if len(item) == number and letter == True and item not in words:
                words.append(item)
    return words

replay = "y"
while replay == "y":
    length = random.randint(5,9)
    options = extractwords("Wordlist",length)
    word = random.choice(options)
    wordarray = []
    for i in word:
        wordarray.append(i)
    dashes = []
    for i in word:
        dashes.append("-")
    print (*dashes, sep='')

    complete=0
    wrongguesses=[]
    guesses = []
    tries=length + 3

    while complete < length and tries > 0:
        guess = input("Please enter a letter:")
        if guess.isalpha() and len(guess) == 1:
            if guess not in wrongguesses and guess not in guesses:
                if guess not in word:
                    print ("Your letter is not in my word.")
                    wrongguesses.append(guess)
                    print ("Wrong letters:", wrongguesses)
                else:
                    for i in range(0,length):
                        if word[i]==guess:
                            dashes[i] = guess
                            complete=complete+1
                guesses.append(guess)
                tries = tries-1          
            else:
                print ("Please enter a letter you haven't entered yet.")
        else:
            print ("Please enter a single letter.")

            
        print ("Tries left:",tries)
        print (*dashes, sep='')

    if tries == 0:
        print ("You lost! The word was:",word)
    if complete == length:
        print ("Good job! You won!")
    replay = input("Do you want to play again? y/n")
                

