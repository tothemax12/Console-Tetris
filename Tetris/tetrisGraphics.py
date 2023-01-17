#Tetris Graphics
import pygame

def getColor(idx):
    pass

def drawBoard(surface, board):
    #I want to draw a square for each index of the board and then change the color depending on what is in that index
    x = 0; 
    y = 0;
    #each square should be 20 by 20, grid is 10 by 20 squares
    for i in range(len(board)):
        if not(i%12):
            y += 10
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(x, y, 20, 20),  2)
        x += 20
