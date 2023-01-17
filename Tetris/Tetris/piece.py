import gameFunctions

class Piece():
    def __init__(self, piece, locationFormulas, collisionPOIS, location):
        self.piece = piece
        self.locationFormulas = locationFormulas
        self.collisionPOI = collisionPOIS
        self.orientation = 1
        self.location = location

    def getLocation(self):
        #return the location for each unique orientation where i is the location and the "formulas" are a list of ints, 
        #kind of hacking together the current location with the correct index
        locationArr = [0, 0, 0, 0];
        for i in range(4):
            locationArr[i] = self.location + self.locationFormulas[self.orientation-1][i]
        return locationArr

    #rotate check will see if there is any spots that would block the rotation of a piece, if there is return false (can't do the rotation) Note: we don't/should check the location of i because
    #the piece rotates around i and will be there at any rotation.
    def rotateCheck(self):
        #check the locations, except for i, of the rotation were are trying to go to
        #if they are all empty, we are good to rotate!
        #otherwise return false

        #get future spots (for next orientation)
        locationArr = [0, 0, 0, 0];
        for i in range(4):
            locationArr[i] = self.location + self.locationFormulas[self.orientation][i]
        
        #check to see if future spots are already taken
        for i in range(4):
            if gameFunctions.board[locationArr[i]] != 0:
                return False
        return True

    def rotate(self):
        print(self.rotateCheck())
        if (self.rotateCheck()):
            self.orientation += 1
            self.orientation %= 4
            print(self.orientation)
        #location = getPieceLocation(piece, orientation, pieceLocation);
        #if dir == "left":
        #    #check for left collision
        #    for i in range(4):
        #        location[i] -= 1 #if they were to move left
        #        if location[i] != 0: #a space they would go is not free
        #            print("left collision!")une
        #            return True
        #    return False
        #elif dir == "right":
        #    #check for right collision
        #    for i in range(4):
        #        location[i] += 1 #if they were to move right
        #        if location[i] != 0: #a space they would go is not free
        #            print("right collision!")
        #            return True
        #    return False