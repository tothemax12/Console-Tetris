#Tetris V.2
import pygame
import time
import os
import tetrisDev
import gameFunctions
import tetrisGraphics

pygame.init()
pygame.screen = pygame.display.set_mode((400, 800))

#currentPiece = gameFunctions.getNextPiece(gameFunctions.pieceArr)
currentPiece = gameFunctions.pieceArr[1]
def moveDown():
    global currentPiece

    ##if a piece hits the floor/another piece then stop it and spawn a new piece
    if (not gameFunctions.collisionCheck(currentPiece, "down")):
        currentPiece.location += 12
    else:
        currentPiece = gameFunctions.getNextPiece(gameFunctions.pieceArr)
        currentPiece.location = 16 #move the new one back to the top
        gameFunctions.checkForTetris() #see if there was a tetris after a piece was placed

#basic game loop
while (True):
    time.sleep(0.5)
    os.system("cls")
    gameFunctions.erasePiece(currentPiece)
    gameFunctions.eventCheck(currentPiece)
    gameFunctions.drawPiece(currentPiece.piece, currentPiece.getLocation())
    gameFunctions.printBoard()
    tetrisGraphics.drawBoard(pygame.screen, gameFunctions.board)
    if (gameFunctions.gameOverCheck(currentPiece)):
        break
    moveDown()
    ##if a piece hits the floor/another piece then stop it and spawn a new piece
    #if (not gameFunctions.collisionCheck(currentPiece, "down")):
    #    currentPiece.location += 12
    #else:
    #    currentPiece = gameFunctions.getNextPiece(gameFunctions.pieceArr)
    #    currentPiece.location = 16 #move the new one back to the top
    #    gameFunctions.checkForTetris() #see if there was a tetris after a piece was placed
        

#def test():
#    while True:
#        gameFunctions.eventCheck(tPiece, gameFunctions.board)
#test()

#gameFunctions.checkForTetris()