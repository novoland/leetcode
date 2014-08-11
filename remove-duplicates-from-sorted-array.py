class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
    	if not A:
    		return 0 
    	index = 0
    	lastNum = A[0]
    	for x in xrange(1,len(A)):
    		if A[x] != lastNum:
    			index = index + 1
    			A[index] = A[x]    			
    			lastNum = A[x]
    		x = x + 1
    	return index + 1
        