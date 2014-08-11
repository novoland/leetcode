class Solution:
    # @return an integer
    def numTrees(self, n):
        if not n:
            return 1
        result = [0]*(n+1)
        result[0],result[1] = 1,1
        for x in xrange(2,n+1):
             for y in xrange(0,x):
                result[x] += result[y]*result[x-y-1] 
        return result[n]
        