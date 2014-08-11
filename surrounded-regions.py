class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        row,col=len(board),len(board[0])
        stack = set()
        for x in xrange(col):
            if board[0][x] == 'O':
                stack.add((0,x))
            if board[row-1][x] == 'O':
                stack.add((row-1,x))
        for x in xrange(row):
            if board[x][0] == 'O':
                stack.add((x,0))
            if board[x][col-1] == 'O':
                stack.add((x,col-1))
        while stack:
            pos = stack.pop()
            i,j=pos[0],pos[1]
            board[i][j] = 'T'
            if i>0 and board[i-1][j] == 'O':
                stack.add((i-1,j))
            if i<row-1 and board[i+1][j] == 'O':
                stack.add((i+1,j))
            if j>0 and board[i][j-1] == 'O':
                stack.add((i,j-1))
            if j<col-1 and board[i][j+1] == 'O':
                stack.add((i,j+1))
        for x in xrange(row):
            for y in xrange(col):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'T':
                    board[x][y] = 'O'