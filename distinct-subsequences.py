class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if not S or not T:
            return 0 
        elif len(S) < len(T):
            return 0 
        sizeT = len(T)
        sizeS = len(S)
        result = [[0 for i in xrange(sizeS+1)] for j in xrange(sizeT+1)]
        for x in xrange(sizeS+1):
            result[0][x] = 1
        for x in xrange(1,sizeT+1):            
            for y in xrange(1,sizeS+1):
                result[x][y] =result[x-1][y-1] + result[x][y-1] if T[x-1] == S[y-1] else result[x][y-1]
       
        return result[sizeT][sizeS]