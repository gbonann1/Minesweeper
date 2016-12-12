'''
Gianluca Bonanno
Albert Kwok
Final Project
A 53
'''

import random

#Constants
NUMBER_OF_MINES = 10
MAX_BOARD_X = 9
MAX_BOARD_Y = 9
MINE = -1
EMPTY = 0

class Board:
    #Constructor
    #Creates a 2d array and fills it with empty Cell Objects
    def __init__(self, boardX, boardY, emptyCellList):
        self.__board = []
        self.__emptyCellList = []
        listIndex = 0
        for arow in range(boardY):
            row = []
            for acol in range(boardX):
                row.append(emptyCellList[listIndex])
                listIndex += 1
            self.__board.append(row)
        self.__gameOver = False
    #-----------------------------------------------
    #Predicates
    #Check to see if all all non mines are revealed
    def isGameWon(self):
        value = True
        for i in range(MAX_BOARD_X * MAX_BOARD_Y - NUMBER_OF_MINES):
            if not self.__emptyCellList[i].isRevealed():
                value = False
        return value
        
    def getBoard(self):
        return self.__board

    def isGameOver(self):
        return self.__gameOver
    #-----------------------------------------------    
    #Mutators
    #Changes game state to over
    def gameOver(self):
        self.__gameOver = True

    #Reveals all Cells
    def revealAll(self):
        for x in range(MAX_BOARD_X):
            for y in range(MAX_BOARD_Y):
                self.__board[x][y].reveal()
                
    #Randomly creates 10 mines on the board            
    def createMines(self, numMines, boardX, boardY):
        i = 0
        while (i < numMines):
            randomX = random.randint(0, boardX-1)
            randomY = random.randint(0, boardY-1)
            if not self.__board[randomX][randomY].isMine():
                self.__board[randomX][randomY].createMine()
                i += 1
        
    #Calculates the number of surrounding mines for each cell that doesn't
    #contain a mine
    def createCellStates(self, boardX, boardY):
        for y in range(boardY):
            for x in range(boardX):
                if not self.__board[y][x].isMine():
                    self.__emptyCellList.append(self.__board[y][x])
                    if not (y+1 > boardY-1):
                        if self.__board[y+1][x].isMine():
                            self.__board[y][x].incrementState()
                    if not (y-1 < 0):
                        if self.__board[y-1][x].isMine():
                            self.__board[y][x].incrementState()
                    if not (x+1 > boardX-1):
                        if self.__board[y][x+1].isMine():
                            self.__board[y][x].incrementState()
                    if not (x-1 < 0):
                        if self.__board[y][x-1].isMine():
                            self.__board[y][x].incrementState()
                    if not ((y+1 > boardY-1) or (x+1 > boardX-1)):
                        if self.__board[y+1][x+1].isMine():
                            self.__board[y][x].incrementState()
                    if not ((y+1 > boardY-1) or (x-1 < 0)):
                        if self.__board[y+1][x-1].isMine():
                            self.__board[y][x].incrementState()
                    if not ((y-1 < 0) or (x+1 > boardX-1)):
                        if self.__board[y-1][x+1].isMine():
                            self.__board[y][x].incrementState()
                    if not ((y-1 < 0) or (x-1 < 0)):
                        if self.__board[y-1][x-1].isMine():
                            self.__board[y][x].incrementState()

    #To String for pre GUI testing purposes
    def __str__(self):
        someStr = ''
        for y in range(MAX_BOARD_Y):
            someStr += '\n'
            for x in range(MAX_BOARD_X):
                someStr += str(self.__board[y][x].getState())
        return someStr
