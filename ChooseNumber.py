#Seth Jones
#11/07/2019
#Period 1/2


import random
from time import sleep
divideLines = "------------------------------------------------"

#--------------------------Options----------------------#

def options():
    while True:
        print(divideLines)
        sleep(0.5)
        options = """
Welcome to the almalgamation of Tic Tac Toe and the Number Game.
    Please choose your game mode.
    
    1: You Guess Computer's Number
    2: Computer Guesses Your Number
    3: Play Tic Tac Toe

    4: Quit
    """
        print(options)
        while True:
            op = input("Enter option (1-4): ")
            if op == "1":
                sleep(0.5)
                menu()
                break
            elif op == "2":
                sleep(0.5)
                comset()
            elif op == "3":
                import TicTacToe  
                sleep(1)
                input("\nPress enter to go back.")
                print(divideLines)
                break
            if op == "4":
                print(divideLines)
                quit()
            else:
                sleep(0.5)
                print("Please choose a valid option.\n")
                continue
            

#----------------------Menu---------------------------#

def menu():
    while True:
        print(divideLines)
        menu = """
Play Alone

    Choose your difficulty.

    1: Easy
    2: Medium
    3: Hard
    4: Custom

    5: Quit

    """
        print(menu)
        dif = input("Enter difficulty (1-5): ")
        if dif == "1":
            sleep(0.5)
            print("\nYou picked Easy.")
            rmin = 0
            rmax = 10
            maxTries = 3
            game_loop(rmin,rmax,maxTries,gamesWon,gamesLost)
            break
        elif dif == "2":
            sleep(0.5)
            rmin = 0
            rmax = 100
            maxTries = 5
            print("\nYou picked Medium.")
            game_loop(rmin,rmax,maxTries,gamesWon,gamesLost)
            break
        elif dif == "3":
            sleep(0.5)
            rmin = 0
            rmax = 1000
            maxTries = 10
            print("\nYou picked Hard.")
            game_loop(rmin,rmax,maxTries,gamesWon,gamesLost)
            break
        elif dif == "4":
            while True:
                sleep(0.5)
                minIn = input("\nPlease choose your minimum: ")
                if minIn.isdigit():
                    rmin = int(minIn)
                    break
                else:
                    print("Please choose a valid number.")
            while True:
                maxIn = input("Please choose your maximum: ")
                if maxIn.isdigit():
                    rmax = int(maxIn)
                    break
                else:
                    print("Please choose a valid number.")
            if rmin > rmax:
                print("Please choose a maximum that is more than the minimum.")
                break
            while True:
                tryIn = input("Please choose your try count: ")
                if tryIn.isdigit():
                    maxTries = int(tryIn)
                    game_loop(rmin,rmax,maxTries,gamesWon,gamesLost)
                    
                    break
                else:
                    print("Please choose a valid number.")
        elif dif == "5":
            quit()
        else:
            print("\nPlease choose a number from 1 to 4.")


#-------------------------Assign Number------------------------#
        
def assign_number(rmin,rmax):
    while True:
        sleep(0.5)
        userNum = input(str.format("\nPick a number between {0} and {1}: ",rmin,rmax))
        if userNum.isdigit():
            userNum = int(userNum)
            if userNum >= rmin and userNum <= rmax:
                return userNum
            else:
                sleep(0.5)
                print("Please choose a number in the range.")
                continue
            sleep(0.5)
            print("Invalid choice, try again.")



#-------------------------------Game Loop--------------------------#

def game_loop(rmin,rmax,maxTries,gamesWon,gamesLost):
    tries = 0
    randnum = random.randint(rmin,rmax)
    x = assign_number(rmin,rmax)
    tries += 1
    while tries != maxTries and x != randnum:
        if x > randnum:
            print("Guess lower.")
            if (maxTries - tries) == 1:
                print("You have 1 try left.")
            else:
                print(str.format("You have {} tries left.",(maxTries - tries)))
            
        else:
            print("Guess higher.")
            if (maxTries - tries) == 1:
                print("You have 1 try left.")
            else:
                print(str.format("You have {} tries left.",maxTries - tries))

        x = assign_number(rmin,rmax)
        tries += 1
            
    if x == randnum:
        sleep(0.5)
        print("\nYou have won the game!")
        gamesWon += 1
        sleep(1)
        while True:
            quitChoice = input("Would you like to try again? (y/n): ")
            if quitChoice == "n":
                quit()
            elif quitChoice == "y":
                sleep(1)
                options()
            elif quitChoice == "'y' or 'n'":
                sleep(0.5)
                print("Cheeky.\n")
                continue
            else:
                sleep(0.5)
                print("Please type 'y' or 'n'.\n")
                continue
    else:
        print("You lose!")
        print(str.format("The number was {}.",randnum))
        gamesLost += 1
        sleep(1)
        while True:
            quitChoice = input("Would you like to try again? (y/n): ")
            if quitChoice == "y":
                game_loop(rmin,rmax,maxTries,gamesWon,gamesLost)
            elif quitChoice == "n":
                sleep(1)
                options()
            elif quitChoice == "'y' or 'n'":
                sleep(0.5)
                print("Cheeky.\n")
                continue
            else:
                sleep(0.5)
                print("Please type 'y' or 'n'.\n")
                continue
def comset():
    print(divideLines)
    sleep(1)
    print("""Welcome to the computer number guessing game! You will think
of a number, then the computer will try to guess it based on
your inputs. You will enter 'h' for higher, 'l' for lower,
and 'e' for equal.\n""")
    while True:
        sleep(0.5)
        minIn = input("Please choose your minimum: ")
        if minIn.isdigit():
            rmin = int(minIn)
            break
        else:
            sleep(0.5)
            print("Please choose a valid number.\n")
            continue
    while True:
        sleep(0.5)
        maxIn = input("Please choose your maximum: ")
        if maxIn.isdigit():
            rmax = int(maxIn)
            break
        elif rmin >= rmax:
            sleep(0.5)
            print("Please choose a maximum that is more than your minimum.\n")
            continue
        else:
            sleep(0.5)
            print("Please choose a valid number.\n")
            continue
    while True:
        sleep(0.5)
        tryIn = input("Please choose the amount of guesses the computer has: ")
        if tryIn.isdigit:
            maxTries = tryIn
            comloop(rmin,rmax,maxTries)
            break
        else:
            sleep(0.5)
            print("Please choose a valid number.\n")
def comloop(rmin,rmax,maxTries):
    tries = 0
    while maxTries != tries:
        inCom = round((rmax - rmin + 1)/2)
        print(divideLines)
        print(str.format("I'm thinking your number is {}.",inCom))
        sleep(0.5)
        tries += 1
        while maxTries != tries:
            print(tries)
            print(maxTries)
            sleep(0.5)
            hl = input("Is this number higher, lower, or equal('h', 'l', or 'e')? ")
            if hl == "l":
                sleep(0.5)
                rmin = inCom
                inCom = round(((rmax - rmin + 1)/2) + inCom)
                print(divideLines)
                print(str.format("I'm thinking your number is {}.",inCom))
                tries += 1
            elif hl == "h":
                sleep(0.5)
                rmax = inCom
                inCom = round(inCom - ((rmax - rmin + 1)/2))
                print(divideLines)
                print(str.format("I'm thinking your number is {}.",inCom))
                tries += 1
            elif hl == "e":
                sleep(0.5)
                print("Nice. We did it.")
                break
            else:
                print("Please type 'h', 'l', ir 'e'.")
                continue
        else:
            sleep(0.5)
            print("I've run out of tries. I'm sorry.")
            break
        while True:
            quitChoice = input("Would you like to try again? (y/n): ")
            if quitChoice == "n":
                options()
            elif quitChoice == "y":
                sleep(1)
                comset()
            elif quitChoice == "'y' or 'n'":
                sleep(0.5)
                print("Cheeky.\n")
                continue
            else:
                sleep(0.5)
                print("Please type 'y' or 'n'.\n")
                continue
    else:
        sleep(1)
        print("The computer has run out of guesses.")
        while True:
            quitChoice = input("Would you like to try again? (y/n): ")
            if quitChoice == "n":
                options()
            elif quitChoice == "y":
                sleep(1)
                comset()
            elif quitChoice == "'y' or 'n'":
                sleep(0.5)
                print("Cheeky.\n")
                continue
            else:
                sleep(0.5)
                print("Please type 'y' or 'n'.\n")
                continue
        
    
                
                
    
        
            
    
    
        
sleep(0.5)
options()
