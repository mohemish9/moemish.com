from Board import *
from Player import *

def main():
    """ Human versus AI game.  No code to write here! """
    k = int(input("Enter ply (level from 0 to 5): "))
    px = "human"
    po = Player("O", "LEFT", k)
    b = Board(7, 6)
    playGame(b, px, po)
    
def playGame(b, px, po):
    """ plays a game of Connect Four
        p1 and p2 are objects of type Player OR
        the string 'human'.
    """
    
    nextPieceToMove = ["X","O"]  
    nextPlayerToMove = [px,po]
    n=0
    # FILL IN CODE HERE
    while True:
        if  b.isFull() == False and nextPlayerToMove[n%2] == "human":
            move = askformove(b)
            b.addMove(move, nextPieceToMove[n%2])
            print(b)
            if b.winsFor(nextPieceToMove[n%2]):
                nextPieceToMove = nextPieceToMove[n%2]
                print(nextPieceToMove + " wins!")
                break
        elif not b.isFull():
            move = nextPlayerToMove[n%2].nextMove(b)
            b.addMove(move, nextPieceToMove[n%2])
            print(b)
            if b.winsFor(nextPieceToMove[n%2]):
                nextPieceToMove = nextPieceToMove[n%2]
                print(nextPieceToMove + " wins!")
                break
        else:
            nextPieceToMove = "D"
            break
        n = 1+n 
    return(b.data, nextPieceToMove)
    
def askformove(b):
    """asks human player for a move and makes sure it is a valid one"""
    while True:
        print(b)
        userInput = input("enter your move ")
        try:
            userInput= int(userInput)
            assert(userInput <= b.width )
            assert(b.allowsMove(userInput))
        except (ValueError,AssertionError):
            print("enter a diff move")
            continue
        return userInput 