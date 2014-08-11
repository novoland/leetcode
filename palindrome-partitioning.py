class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
    	if not s:
    		return []
    	size = len(s)
    	if size == 1:
    		return [[s]]
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
    	stack = [0]
    	top = 0
    	index = 1
    	data = []    	
    	while stack: 		
    		cur = stack[top]
    		# print cur
    		# print index
    		# print "---"     		
    		if result[cur][index]:
    			stack.append(index)
    			top += 1
    			if index == size:
    				# print stack
    				t = []
    				for x in xrange(0,top):
    					t.append(s[stack[x]:stack[x+1]])
    				data.append(t)
	    			index = stack.pop() + 1
	    			top -= 1
    		index += 1
    		if index > size:
    			index = stack.pop() + 1
    			top -= 1     		
    	return data
