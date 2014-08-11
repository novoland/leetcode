class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if not board:
            return False
        for x in xrange(0,len(board),1):
            if not self.checkRow(board,x):
                return False
        for x in xrange(0,len(board[0]),1):
            if not self.checkCol(board,x):
                return False    
        for x in xrange(0,9,3):
            for y in xrange(0,9,3):
                 if not self.check9(board,x,y):
                     return False
        return True
        
    def checkRow(self,board,i):
        tmp = set()
        for x in xrange(0,len(board[0]),1):
            if  board[i][x] != '.':
                if board[i][x] in tmp:
                    return False
                else:
                    tmp.add(board[i][x])
        return True

    def checkCol(self,board,i):
        col = set()
        for x in xrange(0,len(board),1):
            if  board[x][i] != '.':
                if board[x][i] in col:
                    return False
                else:
                    col.add(board[x][i])
        return True

    def check9(self,board,xStart,yStart):
        tmp = set()
        for x in xrange(xStart,xStart+3,1):
            for y in xrange(yStart,yStart+3,1):
                t = board[x][y]
                if  t != '.':
                    if t in tmp:
                        return False
                    else:
                        tmp.add(t)
        return True
                