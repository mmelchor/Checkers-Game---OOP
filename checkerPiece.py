#####################################################
# Miguel Melchor (03/19/2014)
# checkerPiece.py
# Class for the checker pieces
####################################################
from graphics import*
import math


def findPiece(lst,x,y):
        idx = 0
        Loc = lst[0].getLoc()
        distance = math.sqrt((x-Loc[0])**2 + (y-Loc[1])**2)
        for i in range(0,len(lst)):
            Loc = lst[i].getLoc()
            d = math.sqrt((x-Loc[0])**2 + (y-Loc[1])**2)
            if d < distance: 
                distance = d
                idx = i

        return (lst[idx],distance,lst[idx].getID)


class Piece:
    #Implements the pieces of the board
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id = 0
        self.pic = ""

    def getLoc(self):
        return (self.x,self.y)
    
    def setLoc(self,newX,newY):
        self.x = newX
        self.y = newY
    
    def getID(self):
        return self.id
    
    def setID(self,ID):
        self.id = ID
    
    def setImage(self,point,pic,win):
        self.pic = pic
        self.image = Image(point,pic)
        self.image.draw(win)
        
    def getPic(self):
        return self.pic
        
    def deleteImage(self,win):
        self.image.undraw()

    def move(self,ally,enemy,x,y):
        #check who the piece thats about to be eaten belongs to
        check_ally = findPiece(ally,x,y)
        check_enemy = findPiece(enemy,x,y)
        
        if check_ally[1] < check_enemy[1] and check_ally[2] == 1:
            #if you return this then you are trying to eat your own piece
            return False

        
        #else there is nothing
        self.setLoc(x,y)
        
