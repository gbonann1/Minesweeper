'''
Gianluca Bonanno
Albert Kwok
Final Project
A 53
'''

import Cell
import Board
import random
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

#Constants
NUMBER_OF_MINES = 10
MAX_BOARD_X = 9
MAX_BOARD_Y = 9
MINE = -1
EMPTY = 0

class MinesweeperGUI:
    def __init__(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.configure(background = "#000000")
        self.__mainWindow.title("Minesweeper 1.1")
        #Creates 81 buttons for the 9x9 grid.
        self.__button1 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(1,0,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button1.grid(row=0, column=0)
        self.__button2 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(2,1,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button2.grid(row=1, column=0)
        self.__button3 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(3,2,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button3.grid(row=2, column=0)
        self.__button4 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(4,3,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button4.grid(row=3, column=0)
        self.__button5 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(5,4,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button5.grid(row=4, column=0)
        self.__button6 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(6,5,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button6.grid(row=5, column=0)
        self.__button7 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(7,6,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button7.grid(row=6, column=0)
        self.__button8 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(8,7,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button8.grid(row=7, column=0)
        self.__button9 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(9,8,0), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button9.grid(row=8, column=0)
        self.__button10 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(10,0,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button10.grid(row=0, column=1)
        self.__button11 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(11,1,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button11.grid(row=1, column=1)
        self.__button12 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(12,2,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button12.grid(row=2, column=1)
        self.__button13 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(13,3,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button13.grid(row=3, column=1)
        self.__button14 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(14,4,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button14.grid(row=4, column=1)
        self.__button15 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(15,5,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button15.grid(row=5, column=1)
        self.__button16 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(16,6,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button16.grid(row=6, column=1)
        self.__button17 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(17,7,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button17.grid(row=7, column=1)
        self.__button18 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(18,8,1), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button18.grid(row=8, column=1)
        self.__button19 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(19,0,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button19.grid(row=0, column=2)
        self.__button20 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(20,1,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button20.grid(row=1, column=2)
        self.__button21 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(21,2,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button21.grid(row=2, column=2)
        self.__button22 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(22,3,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button22.grid(row=3, column=2)
        self.__button23 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(23,4,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button23.grid(row=4, column=2)
        self.__button24 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(24,5,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button24.grid(row=5, column=2)
        self.__button25 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(25,6,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button25.grid(row=6, column=2)
        self.__button26 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(26,7,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button26.grid(row=7, column=2)
        self.__button27 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(27,8,2), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button27.grid(row=8, column=2)
        self.__button28 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(28,0,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button28.grid(row=0, column=3)
        self.__button29 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(29,1,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button29.grid(row=1, column=3)
        self.__button30 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(30,2,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button30.grid(row=2, column=3)
        self.__button31 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(31,3,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button31.grid(row=3, column=3)
        self.__button32 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(32,4,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button32.grid(row=4, column=3)
        self.__button33 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(33,5,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button33.grid(row=5, column=3)
        self.__button34 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(34,6,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button34.grid(row=6, column=3)
        self.__button35 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(35,7,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button35.grid(row=7, column=3)
        self.__button36 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(36,8,3), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button36.grid(row=8, column=3)
        self.__button37 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(37,0,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button37.grid(row=0, column=4)
        self.__button38 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(38,1,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button38.grid(row=1, column=4)
        self.__button39 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(39,2,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button39.grid(row=2, column=4)
        self.__button40 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(40,3,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button40.grid(row=3, column=4)
        self.__button41 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(41,4,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button41.grid(row=4, column=4)
        self.__button42 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(42,5,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button42.grid(row=5, column=4)
        self.__button43 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(43,6,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button43.grid(row=6, column=4)
        self.__button44 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(44,7,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button44.grid(row=7, column=4)
        self.__button45 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(45,8,4), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button45.grid(row=8, column=4)
        self.__button46 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(46,0,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button46.grid(row=0, column=5)
        self.__button47 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(47,1,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button47.grid(row=1, column=5)
        self.__button48 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(48,2,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button48.grid(row=2, column=5)
        self.__button49 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(49,3,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button49.grid(row=3, column=5)
        self.__button50 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(50,4,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button50.grid(row=4, column=5)
        self.__button51 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(51,5,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button51.grid(row=5, column=5)
        self.__button52 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(52,6,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button52.grid(row=6, column=5)
        self.__button53 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(53,7,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button53.grid(row=7, column=5)
        self.__button54 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(54,8,5), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button54.grid(row=8, column=5)
        self.__button55 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(55,0,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button55.grid(row=0, column=6)
        self.__button56 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(56,1,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button56.grid(row=1, column=6)
        self.__button57 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(57,2,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button57.grid(row=2, column=6)
        self.__button58 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(58,3,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button58.grid(row=3, column=6)
        self.__button59 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(59,4,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button59.grid(row=4, column=6)
        self.__button60 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(60,5,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button60.grid(row=5, column=6)
        self.__button61 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(61,6,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button61.grid(row=6, column=6)
        self.__button62 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(62,7,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button62.grid(row=7, column=6)
        self.__button63 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(63,8,6), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button63.grid(row=8, column=6)
        self.__button64 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(64,0,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button64.grid(row=0, column=7)
        self.__button65 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(65,1,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button65.grid(row=1, column=7)
        self.__button66 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(66,2,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button66.grid(row=2, column=7)
        self.__button67 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(67,3,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button67.grid(row=3, column=7)
        self.__button68 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(68,4,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button68.grid(row=4, column=7)
        self.__button69 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(69,5,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button69.grid(row=5, column=7)
        self.__button70 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(70,6,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button70.grid(row=6, column=7)
        self.__button71 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(71,7,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button71.grid(row=7, column=7)
        self.__button72 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(72,8,7), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button72.grid(row=8, column=7)
        self.__button73 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(73,0,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button73.grid(row=0, column=8)
        self.__button74 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(74,1,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button74.grid(row=1, column=8)
        self.__button75 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(75,2,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button75.grid(row=2, column=8)
        self.__button76 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(76,3,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button76.grid(row=3, column=8)
        self.__button77 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(77,4,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button77.grid(row=4, column=8)
        self.__button78 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(78,5,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button78.grid(row=5, column=8)
        self.__button79 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(79,6,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button79.grid(row=6, column=8)
        self.__button80 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(80,7,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button80.grid(row=7, column=8)
        self.__button81 = Button(self.__mainWindow, borderwidth=1, \
                            command = lambda: self.cellClick(81,8,8), padx = 6, bd = 2, bg='#0000ff', text = "  ")
        self.__button81.grid(row=8, column=8)
        
        self.__buttonList = [self.__button1, self.__button2, self.__button3, self.__button4,
                             self.__button5, self.__button6, self.__button7, self.__button8,
                             self.__button9, self.__button10, self.__button11, self.__button12,
                             self.__button13, self.__button14, self.__button15, self.__button16,
                             self.__button17, self.__button18, self.__button19, self.__button20,
                             self.__button21, self.__button22, self.__button23, self.__button24,
                             self.__button25, self.__button26, self.__button27, self.__button28,
                             self.__button29, self.__button30, self.__button31, self.__button32,
                             self.__button33, self.__button34, self.__button35, self.__button36,
                             self.__button37, self.__button38, self.__button39, self.__button40,
                             self.__button41, self.__button42, self.__button43, self.__button44,
                             self.__button45, self.__button46, self.__button47, self.__button48,
                             self.__button49, self.__button50, self.__button51, self.__button52,
                             self.__button53, self.__button54, self.__button55, self.__button56,
                             self.__button57, self.__button58, self.__button59, self.__button60,
                             self.__button61, self.__button62, self.__button63, self.__button64,
                             self.__button65, self.__button66, self.__button67, self.__button68,
                             self.__button69, self.__button70, self.__button71, self.__button72,
                             self.__button73, self.__button74, self.__button75, self.__button76,
                             self.__button77, self.__button78, self.__button79, self.__button80,
                             self.__button81]
        tkinter.mainloop()

    #Event Handlers
    #Command that runs when a cell is clicked
    def cellClick(self, pos, x, y):
        if not newBoard.isGameOver():
            b = self.__buttonList[pos-1]
            newBoard.getBoard()[x][y].reveal()
            if newBoard.getBoard()[x][y].isMine():
                newBoard.gameOver()
                newBoard.revealAll()
                self.revealButtons()
                self.__gameStateMessage = messagebox.showinfo("Game Over", "You Blew Up!")
            elif newBoard.isGameWon():
                newBoard.gameOver()
                self.__gameStateMessage = messagebox.showinfo("Victory", "You Won!")
                newBoard.revealAll()
                self.revealButtons()  
            elif newBoard.getBoard()[x][y].getState() == 0:
                newBoard.getBoard()[x][y].reveal()
                self.revealAdjacentZero(pos-1, x, y)
                b.configure(text = str(newBoard.getBoard()[x][y].getState()),fg = '#ffffff')                      
            else:
                newBoard.getBoard()[x][y].reveal()
                b.configure(text = str(newBoard.getBoard()[x][y].getState()),fg = '#ffffff')
            
    #Reveals all cells when the game is won/lost
    def revealButtons(self):
        listIndex = 0
        for x in range(MAX_BOARD_X):
            for y in range(MAX_BOARD_Y):
                b = self.__buttonList[listIndex]
                if newBoard.getBoard()[y][x].getState() == -1:
                    b.configure(bg = '#ff0000')
                else:
                    b.configure(text = str(newBoard.getBoard()[y][x].getState()), fg = '#ffffff' )
                listIndex += 1

    #Reveal everything adjacent to a 0
    def revealAdjacentZero(self, pos, x, y):
        if x > 0:
            b = self.__buttonList[pos-1]
            b.configure(text = str(newBoard.getBoard()[x-1][y].getState()),fg = '#ffffff')
            newBoard.getBoard()[x-1][y]
            newBoard.getBoard()[x-1][y].reveal()
            #if newBoard.getBoard()[x-1][y].getState() == 0:
                #self.revealAdjacentZero(pos-1, x-1, y)
        if x < 8:
            b = self.__buttonList[pos+1]
            b.configure(text = str(newBoard.getBoard()[x+1][y].getState()),fg = '#ffffff')
            newBoard.getBoard()[x+1][y].reveal()
            #if newBoard.getBoard()[x+1][y].getState() == 0:
                #self.revealAdjacentZero(pos+1, x+1, y)
        if y > 0:
            b = self.__buttonList[pos - 9]
            b.configure(text = str(newBoard.getBoard()[x][y-1].getState()),fg = '#ffffff')
            newBoard.getBoard()[x][y-1].reveal()
            #if newBoard.getBoard()[x][y-1].getState() == 0:
                #self.revealAdjacentZero(pos-9, x, y-1)
        if y < 8:
            b = self.__buttonList[pos + 9]
            b.configure(text = str(newBoard.getBoard()[x][y+1].getState()),fg = '#ffffff')
            newBoard.getBoard()[x][y+1].reveal()
            #if newBoard.getBoard()[x][y+1].getState() == 0:
                #self.revealAdjacentZero(pos+9, x, y+1)
        if x > 0 and y > 0:
            b = self.__buttonList[pos -1 - 9]
            b.configure(text = str(newBoard.getBoard()[x-1][y-1].getState()),fg = '#ffffff')
            newBoard.getBoard()[x-1][y-1].reveal()
        if x > 0 and y < 8:
            b = self.__buttonList[pos -1 + 9]
            b.configure(text = str(newBoard.getBoard()[x-1][y+1].getState()),fg = '#ffffff')
            newBoard.getBoard()[x-1][y+1].reveal()
        if x < 8 and y > 0:
            b = self.__buttonList[pos +1 - 9]
            b.configure(text = str(newBoard.getBoard()[x+1][y-1].getState()),fg = '#ffffff')
            newBoard.getBoard()[x+1][y-1].reveal()
        if x < 8 and y < 8:
            b = self.__buttonList[pos +1 + 9]
            b.configure(text = str(newBoard.getBoard()[x+1][y+1].getState()), fg = '#ffffff')
            newBoard.getBoard()[x+1][y+1].reveal()

                        
def main():
    emptyCellList = []
    #Creates cell objects for every (x,y) coord on the board
    #Adds these objects to a list
    for i in range(MAX_BOARD_X * MAX_BOARD_Y):
        i = Cell.Cell()
        emptyCellList.append(i)
    global newBoard
    newBoard = Board.Board(MAX_BOARD_X, MAX_BOARD_Y, emptyCellList)
    newBoard.createMines(NUMBER_OF_MINES, MAX_BOARD_X, MAX_BOARD_Y)
    newBoard.createCellStates(MAX_BOARD_X, MAX_BOARD_Y)
    MinesweeperGUI()

main()
