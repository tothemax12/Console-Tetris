#Tetris Piece Definitions
import piece

lPiece = piece.Piece(
                     [2, 2, 2, 2], 
                     [[-1, 0, 1, 13], [-12, 0, 12, 11], [-13, -1, 0, 1], [12, 0, -12, -11]], 
              
                     {0: {
                         "left": [-13, -1, 11],
                         "right": [-10, 1, 13],
                         "down": [1, 24]
                         },
                      1: {
                         "left": [12, -2],
                         "right": [2, 14],
                         "down": [11, 12, 25]
                         },
                      2: {
                         "left": [-13, -1, 10],
                         "right": [-11, 1, 13],
                         "down": [23, 24]
                         },
                      3: {
                         "left": [-2, -14],
                         "right": [2, -12],
                         "down": [11, 12, 13]
                         },
                      }, 
                     16)

tPiece = piece.Piece(
                     [3, 3, 3, 3], 
                     [[-1, 0, -12, 1], [-12, 0, 1, 12], [-1, 0, 12, 1], [-1, 0, -12, 12]], 
              
                     {0: {
                         "left": [-2, -13, 11],
                         "right": [-11, 1, 13],
                         "down": [24, 11]
                         },
                      1: {
                         "left": [-2, -13],
                         "right": [-11, 2],
                         "down": [11, 12, 13]
                         },
                      2: {
                         "left": [-13, -1, 11],
                         "right": [-11, 2, 13],
                         "down": [24, 13]
                         },
                      3: {
                         "left": [-2, 11],
                         "right": [2, 13],
                         "down": [11, 24, 13]
                         },
                      }, 
                     16)
