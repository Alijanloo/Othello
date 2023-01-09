from random import randint

class Tra_tab:

    def __init__(self, m, n) -> None:
        self.ZobristTable = self.init_table(m, n)
        self.mapTable = dict() # an empty initializing dictionary

    def init_table(m, n):
        table = []
        for i in range(m):
            table.append([])
            for j in range(n):
                table[i].append([])
                for k in range(2):
                    val = randint(0, 2**64)
                    table[i][j].append(val)
        return table
    
    def computeHash(self, board):
        h = 0
        for i in len(board):
            for j in len(board[0]):
                if board[i][j] == 'W':
                    h ^= self.ZobristTable[i][j][0]
                if board[i][j] == 'B':
                    h ^= self.ZobristTable[i][j][1]
        return h
    
    def add(self, hash, value):
        self.mapTable[hash] = value
    
    def get(self, hash):
        """
        returns None if the given hash wasn't in the map table or if it was, returns it's value
        """
        try:
            value = self.mapTable[hash]
            return value
        except:
            return None