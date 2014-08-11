class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return
        rowlen = len(matrix)
        collen = len(matrix[0])
        row = set()
        col = set()
        for x in xrange(rowlen):
            for y in xrange(collen):
                if matrix[x][y] == 0:
                    row.add(x)
                    col.add(y)
        for x in xrange(rowlen):
            for y in xrange(collen):
                if (x in row) or (y in col):
                    matrix[x][y] = 0