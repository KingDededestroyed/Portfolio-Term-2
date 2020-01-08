#Tic Tac Toe
#Seth Jones
#11/07/2019
#Period 1/2
#-----------------Imports---------------#
from time import sleep
import random

#----------------Global Constants--------------#
divideLines = "------------------------------------------------"
carrots =     "v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v-v"
X = "X"
O = "O"
squareNum = 9
tie = "Tie"
empty = " "

def instructions():
    sleep(0.5)
    print(divideLines)
    print("""Welcome to Tic Tac Toe!

    You and a computer are going to play Tic Tac Toe.
    There will be a 9x9 board on which you must score
    a row or column of your letter, which will either
    be X or O, of which X will go first. Each space
    has its own number assignment.

        |---|---|---|
        | 1 | 2 | 3 |
        |---|---|---|
        | 4 | 5 | 6 |
        |---|---|---|
        | 7 | 8 | 9 |
        |---|---|---|\n""")
    
    input("Press enter to continue.\n")
    sleep(0.5)

    print("""   The first to get three in a row-- Diagonally,
    horizontally, or vertically-- will win!

        |---|-|-|---|
        | O | X | O |
        |---|-|-|---|
        | X | X | O |
        |---|-|-|---|
        |   | X |   |
        |---|-|-|---|

    It is also possible to end in a tie.\n""")
    
    while True:
        sleep(0.5)
        letter = input("Would you like to play as X or O? ")
        if letter == "X" or letter == "x":
            sleep(0.5)
            human = X
            comp = O
            print("You picked X.")
            you_first()
            game(board,human,comp,winner)
            break
        elif letter == "O" or letter == "o":
            sleep(0.5)
            human = O
            comp = X
            print("You picked O.")
            comp_first()
            game(board,human,comp,winner)
            break
        else:
            print("You must pick X or O.\n")
            
def yes_no(question):
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
        x = response[0]
        return x


def new_game():
    board = []
    for i in range(squareNum):
        board.append(empty)
    return board

#-----------------------------Actual Game Stuff---------------------------#

def game(board,human,comp,winner):
    while True:
        sleep(0.5)
        print(carrots)
        board = new_game()
        print("""
        |---|---|---|
        | 1 | 2 | 3 |
        |---|---|---|
        | 4 | 5 | 6 |
        |---|---|---|
        | 7 | 8 | 9 |
        |---|---|---|
        """)
        
        while empty in board:
            winner(board)
            if human == X:
                if winner(board) != X and winner(board) != O:
                    man_turn(board,human)
                    winner(board)
                else:
                    win_conditions(winner,human,comp,board)
                if winner(board) != X and winner(board) != O:
                    comp_turn(board,comp,human,winner)
                    winner(board)
                else:
                    win_conditions(winner,human,comp,board)
            else:
                if winner(board) != X and winner(board) != O:
                    comp_turn(board,comp,human,winner)
                    winner(board)
                else:
                    win_conditions(winner,human,comp,board)
                if winner(board) != X and winner(board) != O:
                    man_turn(board,human)
                    winner(board)
                else:
                    win_conditions(winner,human,comp,board)
        else:
            if winner(board) != X and winner(board) != O:
                sleep(1)
                print(divideLines)
                print("This game has ended in a tie.")
                print(divideLines)
                sleep(1)
                leave()
            else:
                win_conditions(winner,human,comp,board)

    else:
        print("You won!")

def man_turn(board,human):
    while True:
        print(divideLines)
        marked = input("Pick a spot(1-9): ")
        try:
            play = int(marked)
            break
        except ValueError:
            sleep(0.5)
            print("Please enter a valid number.\n")
    if play <= 9 and play > 0:
        if board[play-1] == empty:
            board[play-1] = human
            sleep(0.5)
            print(carrots)
            print(str.format("""
        |---|---|---|
        | {0} | {1} | {2} |
        |---|---|---|
        | {3} | {4} | {5} |
        |---|---|---|
        | {6} | {7} | {8} |
        |---|---|---|
        """,
                         board[0],
                         board[1],
                         board[2],
                         board[3],
                         board[4],
                         board[5],
                         board[6],
                         board[7],
                         board[8]))
        else:
            sleep(0.5)
            print("That spot has already been taken.\n")
            man_turn(board,human)
    else:
        print("Please choose a number from 1 to 9.\n")
        man_turn(board,human)
def comp_turn(board,comp,human,winner):
    boardCopy = board[:]
    while empty in board:
        while True:
            comMoves = [4,7,5,3,1,8,6,2,0]
                    
            for move in comMoves:
                boardCopy[move] = human
                if winner(boardCopy) == human:
                    if board[move] == empty:
                        comPlay = move
                boardCopy[move] = empty
                    
            for move in comMoves:
                boardCopy[move] = comp
                if winner(boardCopy) == comp:
                    if board[move] == empty:
                        comPlay = move
                boardCopy[move] = empty

            for move in comMoves:
                if board[move] == empty:
                    comPlay = move
                
            if board[comPlay] == empty:
                board[comPlay] = comp
                break
            
            else:
                continue
        sleep(1)
        print(divideLines)
        print(str.format("I have chosen square {}.",comPlay + 1))
        print(carrots)
        sleep(0.5)
        print(str.format("""
        |---|---|---|
        | {0} | {1} | {2} |
        |---|---|---|
        | {3} | {4} | {5} |
        |---|---|---|
        | {6} | {7} | {8} |
        |---|---|---|
    """,
                     board[0],
                     board[1],
                     board[2],
                     board[3],
                     board[4],
                     board[5],
                     board[6],
                     board[7],
                     board[8]))
        break

#---------------------------Order-------------------------------#
        
def you_first():
    human = X
    comp = O
    return comp,human

def comp_first():
    human = O
    comp = X
    return comp,human

def congrat_winner():
    if winner != tie:
        print(str.format("Congratulations! {} has won the game!",winner(board)))

def winner(board):
    ways_to_win = ((0,1,2),(3,4,5),(6,7,8),
                   (0,3,6),(1,4,7),(2,5,8),
                   (0,4,8),(2,4,6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[1]]
            return winner
    if empty not in board:
        return tie
        return None
def win_conditions(winner,human,comp,board):
    winner(board)
    if winner(board) == human:
        sleep(1)
        print(divideLines)
        print("Congratulations, you have won the game!")
        print(divideLines)
    elif winner(board) == comp:
        sleep(1)
        print(divideLines)
        print("You have failed. The computer has won.")
        print(divideLines)
    else:
        sleep(1)
        print(divideLines)
        print("This game has ended in a tie.")
        print(divideLines)
        sleep(1)
    leave()
def leave():
    while True:
        sleep(1)
        qq = input("\nWould you like to play again? (y/n)")
        if qq == "y":
            sleep(0.5)
            instructions()
            break
        elif qq == "n":
            sleep(0.5)
            import ChooseNumber
        else:
            sleep(0.5)
            print("Please type 'y' or 'n'.\n")
def legal_moves(board):
    moves = []
    for square in range(squareNum):
        if board(square) == empty:
            moves.append(square)

    

board = new_game()
instructions()



