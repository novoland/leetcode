class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s:
        	return True
        size = len(s)
        result = [[False for x in xrange(size+1)] for x in xrange(size+1)]
      	for x in xrange(size):
      		if s[x] in dict:
      			result[x][x+1] = True
      	for x in xrange(size-1,-1,-1):
      		for y in xrange(x,size+1):
      			# print x
      			# print y
      			# print "--"
      			if s[x:y] in dict:
      				result[x][y] = True
      				pass
      			for i in xrange(x+1,y):
      				if result[x][i] and result[i][y]:
      					result[x][y] = True
      					break
      	return result[0][size]