class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        result = [[1]*n]*m
        for x in xrange(1,m):
            for y in xrange(1,n):
                result[x][y] = result[x-1][y]+result[x][y-1]
        return result[m-1][n-1]
        