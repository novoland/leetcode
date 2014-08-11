class Solution:
    # @param s, a string
    # @return a list of lists of string
    def minCut(self, s):
    	if not s:
    		return 0
    	size = len(s)
    	if size == 1:
    		return 0
    	result = [[False for x in xrange(size+1)] for y in xrange(size+1)]
    	for x in xrange(size):
    		result[x][x+1] = True
    	for x in xrange(size-1,-1,-1):
    		for y in xrange(x+1,size+1):
    			if y == x+2 and s[x] == s[y-1]:
    				result[x][y] = True
    				pass
    			if s[x] == s[y-1] and result[x+1][y-1]:
    				result[x][y]  = True
    	# print result
    	data = [size-1 for x in xrange(size+1)]   	
    	for x in xrange(size+1):
    		if result[0][x]:
    			data[x] = 0
    			pass
    		for y in xrange(x):
    			if result[y][x] and data[x] > data[y] + 1:
    				data[x] = data[y] + 1
  				
    	return data[size]