class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if not matrix:
            return
        result=[]        
        for x in xrange(0,len(matrix[0])):
            tmp = []
            for y in xrange(len(matrix)-1,-1,-1):
                tmp.append(matrix[y][x])            
            result.append(tmp)
        return result
        