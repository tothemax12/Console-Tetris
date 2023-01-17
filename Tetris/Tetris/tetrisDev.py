import pygame
import gameFunctions
#Tetris Dev Tools

#dev stuff for tetris game

#Board to mess with for developing
#board = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 2, 8, 8, 4, 0, 0, 0, 0, 0, 0, 6,
#         6, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6,
#         6, 4, 4, 4, 0, 4, 0, 4, 4, 4, 4, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
#         6, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 6,
#         6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,]

def devEvents(event, piece, board):
    if event.type == pygame.QUIT:
        raise SystemExit
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:#up
             gameFunctions.erasePiece(piece)
             piece.location -= 12
             gameFunctions.drawPiece(piece.piece, piece.getLocation())
             gameFunctions.printBoard()
        elif event.key == pygame.K_a:#left
             gameFunctions.erasePiece(piece)
             if not gameFunctions.collisionCheck(piece, "left"):
                piece.location -= 1
             gameFunctions.drawPiece(piece.piece, piece.getLocation())
             gameFunctions.printBoard()
        elif event.key == pygame.K_s:#down
             gameFunctions.erasePiece(piece)
             if not gameFunctions.collisionCheck(piece, "down"):
                piece.location += 12
             gameFunctions.drawPiece(piece.piece, piece.getLocation())
             gameFunctions.printBoard()
        elif event.key == pygame.K_d:#right
             gameFunctions.erasePiece(piece)
             if not gameFunctions.collisionCheck(piece, "right"):
                piece.location += 1
             gameFunctions.drawPiece(piece.piece, piece.getLocation())
             gameFunctions.printBoard()
        elif event.key == pygame.K_r:#rotate piece
             gameFunctions.erasePiece(piece)
             piece.rotate()
             gameFunctions.drawPiece(piece.piece, piece.getLocation())
             gameFunctions.printBoard()
             