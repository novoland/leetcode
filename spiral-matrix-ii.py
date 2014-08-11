class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result=[[0 for col in range(n)] for row in range(n)]
        num = 1
        x = y = 0
        down = right = n
        top = left = 0
        while num <= n*n:
            for y in xrange(left,right,1):
                result[x][y] = num
                num += 1
            top += 1
            for x in xrange(top,down,1):            
                result[x][y] = num
                num += 1
            right -=1
            for y in xrange(right-1,left-1,-1):             
                result[x][y] = num
                num += 1
            down -=1
            for x in xrange(down-1,top-1,-1):            
                result[x][y] = num
                num += 1
            left += 1
        return result