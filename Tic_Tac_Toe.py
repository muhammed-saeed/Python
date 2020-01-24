'''
we tell the users what is the position we want to go to it.
and the computer do its move
we pass the location from 0 to 9 

the player plays X and the computer plays an O
'''
import random

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    #insert the letter in our board
    board[pos] = letter
    
    

def spaceIsFree(pos):
    #if the space we want to inter the move in it is free or not
    return board[pos] == ' '
    

def printBoard():
    
    print("   |   |")
    print( ' ' + board[1] + ' | '+ board[2] + ' | ' + board[3])
    print("   |   |")
    print('---------')
    print("   |   |")
    print( ' ' + board[4] + ' | '+ board[5] + ' | ' + board[6])
    print("   |   |")
    print('----------')
    print("   |   |")
    print( ' ' + board[7] + ' | '+ board[8] + ' | ' + board[9])
    print("   |   |")    
    
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    #run will go false if we entered integer between 1 and 9 and its location is free
    while run:
        move = input('Please Select Position to place an \'X\' (1-9) :')
        try:
            move = int(move) 
            #make sure the input is integer
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    #note here we donot need any more to run our input since its already here
                    insertLetter('X', move)
                else:
                    print('sorry this space is occupied!!')
                
            else:
                print('please enter a number within the range! ')
        except:
            print('please enter a number between 1 and 9!!')

def compMove():
    #if there is a move that we can do and end us winning 
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
    #enumerate provide us the indices and the true values such as indices 0 and 'X' and indicies 1 'O' and so on
    move = 0 
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            #this make copy with new space in memeory with the same value of the array
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
    
        
    return move

    
    

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    

def main():
    print('welcome to tic tac toe')
    printBoard()
    while not (isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard()
            
        else:
            print('sorry O\'s won the game this time')
            break
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game ')
                #if there are no more moves the computer can do then this is tie game
            else:
                insertLetter('O', move)
                print('computer placed an \'o\' in postion ', move,':')
                printBoard()
            
        else:
            print(' X\'s won this time! Good Job')
            break
        
            
            
            
    if isBoardFull(board):
        print('Tie Game')
        
while True:
    answer = input('Do you want to play again? (y/n)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break