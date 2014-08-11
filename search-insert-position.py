class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
    	index = 0
    	for a in A:
    		if a == target:
    			return index
    		elif a > target:
    			return index 
    		else:
    			index = index + 1
    	return index
        