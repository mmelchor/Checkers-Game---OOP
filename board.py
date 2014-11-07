#####################################################
# Miguel Melchor (03/19/2014)
# board.py
# Class for the checker board
####################################################
from graphics import*


class Board:
    #Implements the checker board

    def __init__(self,win):
        self.images = {}
        self.drawBoard(win)
            
    def Click(self,win):
        click = win.getMouse()
        return (click.getX(),click.getY())
    

    def drawBoard(self,win):
        for i in range(0,600,75):
            for j in range(0,601,75):
                square = Rectangle(Point(i,j),Point(i+75,j+75))
                if (i%2 ==0 and j%2 == 0) or (i%2 ==1 and j%2 == 1): 
                    square.setFill('white')
                elif (i%2==1 and j%2==0) or (i%2==0 and j%2==1): 
                    square.setFill('black')
                square.draw(win)
                
    def addPlayers(self,Pieces1,Pieces2,win):
        numPlayer1 = 0; numPlayer2 = 0
        for i in range(0,600,75):
            for j in range(0,225,75):
                if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
                    #Creates (x,y)->midpoint for each piece
                    p1 = Point(i+37.5,j+37.5)
                    p2 = Point(i+37.5,j+375+37.5)
                    #Set midpoint for each piece
                    Pieces1[numPlayer1].setLoc(p1.getX(),p1.getY())
                    Pieces2[numPlayer2].setLoc(p2.getX(),p2.getY())
                    
                    Pieces1[numPlayer1].setID(1)
                    Pieces2[numPlayer2].setID(2)

                    Pieces1[numPlayer1].setImage(p1,'Helena.gif',win)
                    Pieces2[numPlayer2].setImage(p2,'Claudia.gif',win)
                

                    numPlayer1 = numPlayer1 + 1
                    numPlayer2 = numPlayer2 + 1

    
        

    def GameOver(self,Pieces1,Pieces2):
        if len(Pieces1) == 0 or len(Pieces2) == 0:
            return True

        
    def winner(lst1,lst2):
        if len(lst1)==0: 
            print("Player 2 wins!")
        elif len(lst2)==0: 
            print("Player 1 wins!")


