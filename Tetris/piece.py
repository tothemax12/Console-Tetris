class Piece():
    def __init__(self, piece, locationFormulas, collisionPOIS):
        self.piece = piece
        self.locationlocationFormulas = locationFormulas
        self.collisionPOIs = collisionPOIS
        self.orientation = 1

    def getLocation(self, i):
        #return the location for each unique orientation where i is the location and the "formulas" are a list of ints
        return (i+locationFormulas[self.orientation]);

    def rotate(self):
             self.orientation += 1
             self.orientation %= 4
