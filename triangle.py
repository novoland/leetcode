class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        for x in xrange(len(triangle)-2,-1,-1):
            tmp = triangle[x]
            for y in xrange(0,len(tmp),1):
                tmp[y] += triangle[x+1][y] if triangle[x+1][y] < triangle[x+1][y+1] else triangle[x+1][y+1]
        return triangle[0][0]
        