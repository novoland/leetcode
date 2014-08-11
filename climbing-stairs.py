class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    	if n < 0:
    		return
    	a = 1
    	b = 1
    	for x in xrange(2,n+1):
    		c = a + b
    		a = b
    		b = c
    	return b