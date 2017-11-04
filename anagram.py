import random
import sys
easy = ["down","exit","ball","book","nose","lazy","maze","code","neck","bank","bulb","walk","milk"]
medium = ["radio","pixel","chair","sword","table","pizza","judge","quest","label","logic","image","juice","earth","igloo"]
hard = ["school","monday","bikes","square","flower","bridge","camera","carpet","castle","cinema","coffee","dancer","desert","escort","guitar","injury","jacket"]
replay="y"
score=0
print ("Hello and welcome to my anagram game! \nYou will be given a scrambled 4, 5 or 6 letter word. \nYou will have 3 tries until you find the answer. \nEasy mode awards one point, medium mode awards 2 points and hard mode awards 3 points. \nWrong answer deducts a point! \nGood Luck!")
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
                score = score+1
                print ("Score:",score)
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
                    
               
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
                score = score+2
                print ("Score:",score)
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
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
                score = score+3
                print ("Score:",score)
                break
            else :
                tries = tries - 1
                if tries > 0:
                    print ("Try again",tries,"tries left,")
                if tries == 0:
                    print ("Wrong guess!")
                    score=score-1
                    print ("Score:",score)
    replay = input("Do you want to play again? y/n")
print ("Total score:",score)
sys.exit()

