import pygame
import tetrisDev
import random
import pieceDefinitions

board = [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6,
         6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,]

pieceArr = [pieceDefinitions.lPiece, pieceDefinitions.tPiece]

def gameOverCheck(currentPiece):
        gameOver = False
        #if they can't move down from initial position it's a game over
        #print(collisionCheck(currentPiece, "down"))
        if collisionCheck(currentPiece, "down") and currentPiece.location == 16:
            gameOver = True
        return gameOver
def eventCheck(piece):
    for event in pygame.event.get():
        #tetrisDev.devEvents(event, piece, board)
        eventHandler(event, piece)

def printBoard():
    for i in range(len(board)):
        if not(i%12):
            print("")
        print(board[i], end="")

#drawPiece takes in a piece [] and a location [] D
def drawPiece(piece, location):
    for i in range(4):#each piece is len = 4
        #print at the location from getPieceLocation
        board[location[i]] = piece[0];

def erasePiece(piece):
    location = piece.getLocation();
    for i in range(4):
        board[location[i]-12] = 0
    #fix the bottom row, kind of a hack
    for i in range(len(board)-1, len(board)-12, -1):
        board[i] = 6

#returns an array of the current moves points of interest to check for collision
def getCollisionPOI(piece, direction):
    pieceLoc = piece.location
    
    orientationPOI = piece.collisionPOI.get(piece.orientation) #grabs the array of POI formulas for the specific piece and orientation
    poiFormulas = orientationPOI.get(direction)
    movePOI = []
    
    for i in range(len(poiFormulas)):
        movePOI += [pieceLoc + poiFormulas[i]] #put together the points of interest for the current location

    return movePOI

#collisionCheck returns True if they would collide and False if the spot is free
def collisionCheck(piece, direction):
        movePOI = getCollisionPOI(piece, direction)
        print(movePOI)
        for i in range(len(movePOI)):
            if board[movePOI[i]] != 0:
                return True
        return False

#get next piece object
def getNextPiece(pieceArr):
    return pieceArr[random.randrange(0, len(pieceArr))]

def eventHandler(event, piece):
    if event.type == pygame.QUIT:
        raise SystemExit
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:#left
             if not collisionCheck(piece, "left"):
                piece.location -= 1
        elif event.key == pygame.K_s:#down
             if not collisionCheck(piece, "down"):
                piece.location += 12
        elif event.key == pygame.K_d:#right
             if not collisionCheck(piece, "right"):
                piece.location += 1
        elif event.key == pygame.K_r:#rotate piece
             piece.rotate()

def eraseFullRows(fullRows):
    firstRowOfTetris = fullRows[0]
    lastRowOfTetris = fullRows[len(fullRows)-1]
    currentRow = firstRowOfTetris
    
    #we want everything from the top of the board to the row above the first row of the Tetris
    while currentRow <= lastRowOfTetris:
        #iterate through each row
        startOfRow = ((currentRow - 1)*12)+1
        endOfRow = startOfRow + 10

        for i in range(startOfRow, endOfRow):#iterate through the current row
                #remove the full rows
                board[i] = 0

        currentRow += 1

def getFullRows():
        bottomRow = 0;
        currentRow = 1
        fullRows = []
        #erase all the full rows and keep track of the bottom-most row you erased
        #for i in range(12):

        #start of the ith row is ((currentRow - 1)*12)+1
        #end of the ith row is (((currentRow - 1)*12)+1) + 9
        while currentRow <= 20:
            #iterate through each row
            startOfRow = ((currentRow - 1)*12)+1
            endOfRow = startOfRow + 10
            fullRowFlag = True

            for i in range(startOfRow, endOfRow):#iterate through the current row
                if (board[i] == 0):#if a spot is  0 the row is not full
                    currentRow += 1
                    fullRowFlag = False
                    break

            if fullRowFlag:
                fullRows += [currentRow]
                currentRow += 1
            else:
                continue
        
        return fullRows
    
def getEverythingAboveTetris(fullRows):
    everythingAboveTetris = []
    currentRow = 1
    rowAboveTetris = fullRows[0]-1
    
    #we want everything from the top of the board to the row above the first row of the Tetris
    while currentRow <= rowAboveTetris:
        #iterate through each row
        startOfRow = ((currentRow - 1)*12)+1
        endOfRow = startOfRow + 10

        for i in range(startOfRow, endOfRow):#iterate through the current row
                #add everything that needs to be moved down to a list
                everythingAboveTetris += [board[i]]

        currentRow += 1
    return everythingAboveTetris

def moveEverythingDown(fullRows, everythingAboveTetris):
    #we need to go to the bottom most row of the tetris that was erased 
    #and then we can start at the end of that row and print everything
    #that was above the tetris backwards to make sure it is line up correctly. 
    #printing backwards sounds easier than trying to find what line we should start printing downwards.
    rowAboveTetris = fullRows[0]-1

    #first we should erase everything that was above the Tetris and we can do that using the 
    #eraseFullRows function just giving it the first row and the row above the tetris
    print("before and after erasing everything above")
    printBoard()
    eraseFullRows([1, rowAboveTetris])
    printBoard()

    currentRow = rowAboveTetris + len(fullRows) #where we actually move it down
    #then print out starting from the end of the last row of the tetris backwards
    j = len(everythingAboveTetris)-1
    while currentRow >= 1:
        #iterate through each row
        startOfRow = ((currentRow - 1)*12)+1
        endOfRow = startOfRow + 9

        for i in range(endOfRow, startOfRow-1, -1):#iterate through the current row
            #put the stuff that was above the tetris where it should be
            
            board[i] = everythingAboveTetris[j]
            if (board[i] == 4):
                print("i = :", i, "j = ", j, "current row = ", currentRow)
                pass
            j -= 1
            
            # if j == 0 we have printed out everything that was above the tetris initially
            if j == 0:
                return 

        currentRow -= 1

#I should iterate through each row and if it's full, add it to the list of full rows
#next we could replace everything in that/those row(s) with 0's (blank spaces) 
#next we could store everything from the top of the board to the row before the top row that was removed
#finally we could print all the stuff we just grabbed starting from the bottom row that was removed
def handleTetris(fullRows):
    everythingAboveTetris = getEverythingAboveTetris(fullRows)
    eraseFullRows(fullRows)
    moveEverythingDown(fullRows, everythingAboveTetris)

#checking for a Tetris is easy enough, just go through the row and if there are no 0's then you have a Tetris
def checkForTetris():

    #print("board before handling Tetris: ")
    #printBoard()

    #if there is a full row, then there is a tetris
    fullRows = getFullRows()
    if len(fullRows) > 0:
        handleTetris(fullRows)

    #print("board after handling Tetris: \n\n")
    #printBoard()