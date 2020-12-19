class Player:

    def __init__(self, ox, tbt, ply):
        self.symbol = ox
        self.tie = tbt
        self.piles = ply
    def __repr__(self):
        output = ""
        output += "Player for "+self.symbol+"\n"
        output += "  with tiebreak: " + self.tieRule+"\n"
        output += "  and ply == " + str(self.ply)+"\n"
        return output
    
    def oppChar(self):
        """ Return the opposite game piece character. """
        if self.symbol == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """ Return the score for the given board b."""
        if b.winsFor(self.symbol): return float(100.0)
        elif b.winsFor(self.oppChar()): return float(0.0)
        else: return float(50.0)
    def tiebreakMove(self, scores):
        """ Return column number of move based on self.tbt. """
        import random
        def highestscore(scores):
            """ Returns the index/indices of the highest number(s) in scores"""
            highest = -100.0
            highestind = ""
            for x in range(len(scores)):
                if scores[x] > highest:
                    highest = scores[x]
                    highestind = str(x)
                elif scores[x] == highest:
                    highestind += str(x)
            return highestind
        ind = highestscore(scores)
        if len(ind) == 1:
            return ind
        elif self.tie == 'LEFT':
            return int(ind[0])
        elif self.tie == 'RIGHT':
            return int(ind[-1])
        else:
            return int(random.choice(ind))

    def scoresFor(self, b):
        """ Return a list of scores for board d, one score for each column
            of the board. """
        output = [float(50.0)] * b.width
        for col in range(b.width):
            if b.allowsMove(col) == False:
                output[col] = float(-1.0)
            elif b.winsFor(self.symbol):
                output[col] = float(100.0)
            elif b.winsFor(self.oppChar()):
                output[col] = float(0.0)
            elif self.piles == 0:
                output[col] = self.scoreBoard(b)
            else:
                b.addMove(col,self.symbol)
                if b.winsFor(self.symbol):
                    output[col] = float(100.0)
                else:
                    if self.piles > 0:
                        if b.isFull():
                            break
                        else:
                            opp = Player(self.oppChar(), self.tie, self.piles-1)
                            output[col] = 100 - max(opp.scoresFor(b))
                b.delMove(col)
        return output
            
    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """
        scores = self.scoresFor(b)
        move = self.tiebreakMove(scores)
        return int(move)



	
