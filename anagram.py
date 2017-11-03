import random
easy = ["down","exit","ball","book","nose","lazy","maze","code","neck","bank","bulb","walk","milk"]
medium = ["radio","pixel","chair","sword","table","pizza","judge","quest","label","logic","image","juice","earth","igloo"]
hard = ["school","monday","bikes","square","flower","bridge","camera","carpet","castle","cinema","coffee","dancer","desert","escort","guitar","injury","jacket"]
replay="y"
while replay == "y":
    level = input("Do you want to play the easy, medium or hard mode?")
    if level == "easy":
        word=random.choice(easy)
        anagram = []
        for i in word:
            anagram.append(i)
        random.shuffle(anagram)
        scrambled = ""
        for i in anagram:
            scrambled = scrambled+i
        tries = 3
        while tries > 0:
            answer = input(scrambled)
            if answer == word:
                print ("Good job!")
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("You lose!")
               
    elif level == "medium":
        word=random.choice(medium)
        anagram = []
        for i in word:
            anagram.append(i)
        random.shuffle(anagram)
        scrambled = ""
        for i in anagram:
            scrambled = scrambled+i
        print ("Good Luck:",scrambled)
        tries = 3
        while tries > 0:
            answer = input(scrambled)
            if answer == word:
                print ("Good job!")
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("You lose!")
    else:
        word=random.choice(hard)
        anagram = []
        for i in word:
            anagram.append(i)
        random.shuffle(anagram)
        scrambled = ""
        for i in anagram:
            scrambled = scrambled+i
        print ("Good Luck:",scrambled)
        tries = 3
        while tries > 0:
            answer = input(scrambled)
            if answer == word:
                print ("Good job!")
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("You lose!")
    replay = input("Do you want to play again? y/n")
print ("Good Bye!")


