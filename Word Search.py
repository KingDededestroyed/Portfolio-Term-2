from time import sleep
import math

wordBank = ["Python","GuidoVanRossum","Array",
            "List","Tuple","Loop",
            "WhileTrue","Datetime","Idle",
            "String","Integer","Return",
            "Break","Syntax","Import",
            "Function","Conditions","Float",
            "Variable","Boolean","True",
            "False"]
questions = ["The main program we use is ____.",
                   "Who created Python?",
                   "A(n) ____ is very similar to a list or tuple.",
                   "A changeable variable which stores many values is a(n) ____.",
                   "An unchangeable variable which stores many values is a(n) ____.",
                   "A line of code which runs through the same code many times is a(n) ____.",
                   "A type of loop which has unbreakable conditions is a(n) ____ loop.",
                   "Importing ____ will help with formatting dates and times.",
                   "The window in which we edit Python code is called ____.",
                   "A variable which holds characters within quotations is called a(n) ____.",
                   "A variable which holds whole numbers is called a(n) ____.",
                   "To grab a variable from a function, one must ____ it.",
                   "To stop a loop from looping, one must input ____.",
                   "A set of rules for a programming language is called ____.",
                   "To grab a function unavailable in base Python, one must ____ it.",
                   "A(n) ____ must be called in order to run its code.",
                   "A loop must have its ____ met in order to run its code.",
                   "A variable which holds decimal numbers is called a(n) ____.",
                   "A(n) ____ holds a piece of data.",
                   "A variable which holds 'True' or 'False' is called a(n) ____.",
                   "____ is one of two words a Boolean variable can hold.",
                   "____ is the other word a Boolean variable can hold."]

grid = """SAPLHRIEZCEIRGTGPOAK
RVYOTTLQOULRWURXPPEA
ZLAIOBVNYVDMNIOWLQLC
QSNLALDEKPIYODPRIXWS
VQIIQIKEAXWJIOMBEHED
ZZRETFWBXJNETVIUROSM
EANINTEGERRQCAPYPEHM
VMOEURTELIHWNNYRYTAS
ANIETBNRUTERURTTKWTK
SAUTTJOOLIGCFOHLNRYF
FRVSEQIOIBNDRSORIAXL
TUPLETPBLXPZXSNNRNJO
OBXZFUAIDEADYUGREVRA
WFXAGUODTJATRMALLLNT
DDLJXUAFZAHNNCQGFNUS
ASRDNGFZXCHHSYMOGOSV
EXPCQVXBHNEKZTSILQNT
ISJKZZAISODJLXPVXILF
BXKGLUJDXHEANUUXYOON
OVWPOFVOMKNZYZFYLQYZ"""

puzzle = "SAPLHRIEZCEIRGTGPOAKRVYOTTLQOULRWURXPPEAZLAIOBVNYVDMNIOWLQLCQSNLALDEKPIYODPRIXWSVQIIQIKEAXWJIOMBEHEDZZRETFWBXJNETVIUROSMEANINTEGERRQCAPYPEHMVMOEURTELIHWNNYRYTASANIETBNRUTERURTTKWTKSAUTTJOOLIGCFOHLNRYFFRVSEQIOIBNDRSORIAXLTUPLETPBLXPZXSNNRNJOOBXZFUAIDEADYUGREVRAWFXAGUODTJATRMALLLNTDDLJXUAFZAHNNCQGFNUSASRDNGFZXCHHSYMOGOSVEXPCQVXBHNEKZTSILQNTISJKZZAISODJLXPVXILFBXKGLUJDXHEANUUXYOONOVWPOFVOMKNZYZFYLQYZ".replace("","  ")
dimen = round(math.sqrt(len(puzzle)/3))*3
gridimen = round(math.sqrt(len(grid)))

def totalreset():
    print("""Welcome to the Digital Word Search! You will be given a question.
To answer it, you must enter the coordinates of the letters of
that word within the word search. Remember to enter the letters
in order. You can press 'r' to get a new word at any time, and
you can press 'w' to keep your word, but reset your answer. To
see words which you have already found, press 's'. If you want
to see the word bank, press 'b'.\n""")
    found = []
    wordChoices = []
    for i in range(len(wordBank)-1):
        wordChoices.append(i*2)
    comBin = []
    for i in range(len(wordBank)):
        comBin.append(questions[i])
        comBin.append(wordBank[i])
    gameloop(found,wordChoices,comBin,)
        
def display_search(puzzle):
    last = 0
    blast = dimen
    row = 0
    print("""
       0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
      ------------------------------------------------------------""")
    while last != (dimen*dimen)/3:
        if row <= 9:
            print(row, " |", puzzle[last:blast])
        else:
            print(row, "|", puzzle[last:blast])
        row = row + 1
        last = last + dimen
        blast = last + dimen

def gameloop(found,wordChoices,comBin):
    while wordChoices != []:
        input("\nPress Enter to continue.\n")
        sleep(1)
        import random
        ques = random.choice(wordChoices)
        ans = ques + 1
        wordChoices.remove(ques)
        getstuff(comBin,ans,ques,found,wordChoices)
    else:
        print("Congratulations! You have finished the game.")
        while True:
            sleep(1)
            dec = input("\nDo you want to play again?(y/n)")
            if dec == "y":
                totalreset()
            elif dec == "n":
                quit()
            else:
                print("Please type 'y' or 'n'.")

def getstuff(comBin,ans,ques,found,wordChoices):
    #------------------------FIRST LETTER(for position)---------------------#
    display_search(puzzle)
    construct = ""
    print("\n" + comBin[ques])
    while True:
        getX = input("\nEnter the X coordinate for your letter: ")
        if getX == "r":
            reset(found,wordChoices,comBin)
        elif getX == "s":
            stats(found)
            continue
        elif getX == "b":
            bank()
            continue
        try:
            fx = int(getX)
        except(ValueError):
            print("Please enter a valid X coordinate.")
            continue
        if fx <= 19:
            break
        else:
            print("Please choose a coordinate from 0-19.")
    while True:
        getY = input("Enter the Y coordinate for your letter: ")
        if getY == "r":
            reset(found,wordChoices,comBin)
        elif getY == "s":
            stats(found)
            continue
        elif getY == "b":
            bank()
            continue
        try:
            fy = int(getY)
        except(ValueError):
            print("Please enter a valid Y coordinate.")
            continue
        if fy <= 19:
            break
        else:
            print("Please choose a coordinate from 0-19.")
    coor = (gridimen * fy) + fx + fy
    letter = grid[coor]
    construct += letter      
    #-----------------------SECOND LETTER(for direction)--------------#
    display_search(puzzle)
    print("\n" + comBin[ques])
    print("\n" + construct)
    while True:
        getX = input("\nEnter the X coordinate for your letter: ")
        if getX == "r":
            reset(found,wordChoices,comBin)
        elif getX == "w":
            print("Your answer has been reset.")
            getstuff(comBin,ans,ques,found,wordChoices)
        elif getX == "s":
            stats(found)
            continue
        elif getX == "b":
            bank()
            continue
        try:
            lx = int(getX)
        except(ValueError):
            print("Please enter a valid X coordinate.")
            continue
        if lx <= 19:
            if lx <= (fx + 1) and lx >= (fx - 1):
                break
            else:
                print("Please choose an adjacent letter.")
            
        else:
            print("Please enter a valid X coordinate.")
    while True:
        getY = input("Enter the Y coordinate for your letter: ")
        if getY == "r":
            reset(found,wordChoices,comBin)
        elif getY == "w":
            print("Your answer has been reset.")
            getstuff(comBin,ans,ques,found,wordChoices)
        elif getY == "s":
            stats(found)
            continue
        elif getY == "b":
            bank()
            continue
        try:
            ly = int(getY)
        except(ValueError):
            print("Please enter a valid Y coordinate.")
            continue
        if ly <= 19:
            if ly <= (fy + 1) and ly >= (fy - 1):
                if ly != fy and lx != fx:
                    direc = "d"
                    break
                elif ly != fy and lx == fx:
                    direc = "v"
                    break
                elif ly == fy and lx != fx:
                    direc = "h"
                    break
                elif ly == fy and lx == fx:
                    print("You aleady chose that!")

            else:
                print("Please choose an adjacent letter.")
        else:
            print("Please enter a valid Y coordinate.")
    coor = (gridimen * ly) + lx + ly
    letter = grid[coor]
    construct += letter      
    #--------------ANY OTHER LETTERS(following direction and position)-------#
    while construct != comBin[ans].upper():
        display_search(puzzle)
        print("\n" + comBin[ques])
        print("\n" + construct)
        while direc != "v":
            if direc == "h":
                print("")
                y = ly
            getX = input("\nEnter the X coordinate for your letter: ")
            if getX == "r":
                reset(found,wordChoices,comBin)
            elif getX == "w":
                print("Your answer has been reset.")
                getstuff(comBin,ans,ques,found,wordChoices)
            elif getX == "s":
                stats(found)
                continue
            elif getX == "b":
                bank()
                continue
            try:
                x = int(getX)
            except(ValueError):
                print("Please enter a valid X coordinate.")
                continue
            if x <= 19:
                if x == lx:
                    print("You already chose that!")
                elif lx >= fx + 1:
                    if x == lx + 1:
                        lx = x
                        break
                    elif x == lx - 1:
                        print("You can't go backwards.")
                        continue
                    else:
                        print("Please choose an adjacent letter.")
                elif lx <= fx - 1:
                    if x == lx + 1:
                        print("You can't go backwards.")
                        continue
                    elif x == lx - 1:
                        lx = x
                        break
                    else:
                        print("Please choose an adjacent letter.")
                else:
                    print("Please choose an adjacent letter.")
            else:
                print("Please enter a valid X coordinate.")
        while direc != "h":
            if direc == "v":
                print("")
                x = lx
            getY = input("Enter the Y coordinate for your letter: ")
            if getY == "r":
                reset(found,wordChoices,comBin)
            elif getY == "w":
                print("Your answer has been reset.")
                getstuff(comBin,ans,ques,found,wordChoices)
            elif getY == "s":
                stats(found)
                continue
            elif getX == "b":
                bank()
                continue
            try:
                y = int(getY)
            except(ValueError):
                print("Please enter a valid Y coordinate.")
                continue
            if y <= 19:
                if y == ly:
                    print("You already chose that!")
                elif ly >= fy + 1:
                    if y == ly + 1:
                        ly = y
                        break
                    elif y == ly - 1:
                        print("You can't go backwards.")
                        continue
                    else:
                        print("Please choose an adjacent letter.")
                elif ly <= fy - 1:
                    if y == ly + 1:
                        print("You can't go backwards.")
                        continue
                    elif y == ly - 1:
                        ly = y
                        break
                    else:
                        print("Please choose an adjacent letter.")
            else:
                print("Please enter a valid Y coordinate.")
            
        coor = (gridimen * y) + x + y
        letter = grid[coor]
        construct += letter      
        
    else:
        found.append(comBin[ans])
        print(str.format("\nCorrect! The word was {}.",comBin[ans].upper()))
        reset(found,wordChoices,comBin)

def reset(found,wordChoices,comBin):
    print("Next word, please.")
    gameloop(found,wordChoices,comBin)

def stats(found):
    print("""
              Words Found
----------------------------------------
""")
    if found != []:
        for word in found:
            print(word)
    else:
        print("*You haven't found any words yet*")
    print(str.format("\nCurrent Score: {0}/{1}", len(found),len(wordBank)))
    print("\n----------------------------------------")

    input("\nPress Enter to continue.")

def bank():
    print("""
            Word Bank
----------------------------------------
""")
    for word in wordBank:
        print(word)
    input("\nPress Enter to continue.")

totalreset()
