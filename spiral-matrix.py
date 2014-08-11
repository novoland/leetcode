class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        rowstart,rowend,colstart,colend=0,row-1,0,col-1
        result = []
        while rowstart <= rowend or colstart <= colend:
            if rowstart <= rowend:
                for x in xrange(colstart,colend+1):
                    result.append(matrix[rowstart][x])
                rowstart += 1
            if colstart <= colend:                    
                for x in xrange(rowstart,rowend+1):
                    result.append(matrix[x][colend])
                colend -= 1
            if rowstart <= rowend:                
                for x in xrange(colend,colstart-1,-1):
                    result.append(matrix[rowend][x])
                rowend -= 1
            if colstart <= colend:                     
                for x in xrange(rowend,rowstart-1,-1):
                    result.append(matrix[x][colstart])
                colstart += 1
        return result