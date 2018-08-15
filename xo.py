
board= [['.','.','.'],['.','.','.'],['.','.','.']]
win= False
finish= False
player=2
currentM='O'
moveErrror=False

def printBoard():
    for i in range(3):
        for j in range(3):
            print(" ", board[i][j], " ", end="")
        print("")

def isFinished():
    for i in range(3):
        for j in range(3):
            if board[j][i]=='.':
                return  False
    return  True


def isEmptyPlace(column,line):
    if board[line][column]=='.':
        return True
    return False



def isWin():
    for i in range(3):
        if(board[i][1]==board[i][2]==board[i][0] and board[i][0]!='.'):
            return  True
    for i in range(3):
        if(board[0][i]==board[1][i]==board[2][i] and board[2][i]!='.'):
            return  True
    for i in range(3):
        if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!='.'):
            return  True
    for i in range(3):
        if(board[0][2]==board[1][1]==board[2][0] and board[2][0]!='.'):
            return  True
    return False

while(win==False and finish==False):
    if(moveErrror==False):
        if(player==2):
            currentM='X'
            player=1
        else:
            currentM='O'
            player=2
    else:
        moveErrror=False
    printBoard()
    print("player ", player)
    mColumn= int(input("column (1-3): "))-1
    mLine= int(input("line (1-3): "))-1
    if(isEmptyPlace(mColumn,mLine)):
        board[mLine][mColumn]=currentM
    else:
        print("your move is illegal- try again")
        moveErrror=True
    win=isWin()
    finish= isFinished()

printBoard()
if win==True:
     print("player",player,"win")
else:
     print("tie")

