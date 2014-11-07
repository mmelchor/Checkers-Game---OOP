from checkerPiece import*
from board import*
from graphics import*



if __name__ == "__main__":
    win = GraphWin('Checkers',600,600)
    win.setBackground('darkBlue')

    Player1 = [] ; Player2 = []
    for i in range(12): Player1.append(Piece()); Player2.append(Piece())  

    board = Board(win)
    board.addPlayers(Player1,Player2,win)

    go = True
    while not board.GameOver(Player1,Player2):

        currPiece = 0
        while go:
            #player one goes until it has moved a piece
            click = board.Click(win)
            #Finds the piece to move
            currPiece = findPiece(Player1,click[0],click[1])
            currImage = currPiece[0].getPic()

            #moves the piece
            move = board.Click(win)
            
            
            #Player1[currPiece].move(to[0],to[1])
            #Player1[currPiece].deleteImage(win)

            #Player1[currPiece].setImage(Point(to[0],to[1]),currImage,win)
            
