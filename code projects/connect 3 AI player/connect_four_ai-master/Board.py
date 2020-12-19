# Connect 4 Game Board

class Board:

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth():
        return self.width

    def getHeight():
        return self.height

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        for n in range(self.height):
            if self.data[self.height-1-n][int(col)] == ' ':
                self.data[self.height-1-n][int(col)] = ox
                break
            
    def clear(self):
        """ Clear the game board of all game pieces. """
        self.data = [[' ']*self.width for r in range(self.height)]
    def setBoard(self, moves):
        """ Set the board using an input string representation. """
        xo = ["X","O"]
        for n in range(len(moves)):
            self.addMove(moves[n] , xo[n%2])            
    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is 
            permitted and return False otherwise. """
        if self.data[0][int(col)] == ' ':
            return True
        return False
            
    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for n in range(self.width):
            if self.allowsMove(n):
                return False
        return True
            
    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """
        for n in range(self.height):
            if self.data[n][int(col)] != ' ':
                self.data[n][int(col)] = ' '
                break
    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """
        # row -
        for row in range(self.height):
            for col in range(self.width-3):
                if self.data[row][col:col+4] == [ox]*4:
                    return True
        #column |
        for row in range(self.height-3):
            for col in range(self.width):
                if self.data[row][col] == ox and self.data[row+1][col] == ox  and self.data[row+2][col] == ox and self.data[row+3][col]==ox: 
                    return True

        #diagonal \
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[row][col] == ox and self.data[row+1][col+1] == ox  and self.data[row+2][col+2] == ox and self.data[row+3][col+3]==ox: 
                    return True
        
        #diagonal /
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[self.height-row-1][col] == ox and self.data[self.height-row-2][col+1] == ox  and self.data[self.height-row-3][col+2] == ox and self.data[self.height-row-4][col+3]==ox: 
                    return True
        return False