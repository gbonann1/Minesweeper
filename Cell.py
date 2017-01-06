'''
Gianluca Bonanno
Albert Kwok
Final Project
A 53
'''

#Constants
NUMBER_OF_MINES = 10
MAX_BOARD_X = 9
MAX_BOARD_Y = 9
MINE = -1
EMPTY = 0

class Cell:
    #Constructor
    def __init__(self):
        self.__state = EMPTY
        self.__revealed = False
        self.__flagged = False
    #-----------------------------------------------
    #Predicates
    #Returns true if the cell is a mine
    def isMine(self):
        return self.__state == MINE
    
    #Returns if the cell is revealed or not
    def isRevealed(self):
        return self.__revealed

    def isFlagged(self):
        return self.__flagged
    #-----------------------------------------------
    #Mutators
    #Sets reveal to true
    def reveal(self):
        self.__revealed = True
        
    #Sets the cell state to the value of a mine
    def createMine(self):
        self.__state = MINE

    #Increases the cell state by 1
    def incrementState(self):
        self.__state += 1

    def flag(self):
        self.__flagged = True

    def unflag(self):
        self.__flagged = False
    #-----------------------------------------------
    #Accessors
    #Returns the cell's state
    def getState(self):
        return self.__state
