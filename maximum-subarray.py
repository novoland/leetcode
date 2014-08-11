class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
    	if not A:
    		return
    	slow = 0
    	maxsum = A[0]
    	rs = 0
    	for x in xrange(0,len(A)):
    		rs += A[x]
    		if rs > maxsum:
    			maxsum = rs
    		while(rs <= 0 and  slow <= x):
    			rs = rs - A[slow]
    			slow = slow + 1
    	return maxsum