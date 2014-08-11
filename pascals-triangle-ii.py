class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        index = 0
        while index < rowIndex:
            result.insert(0,1)
            for x in xrange(1,len(result)-1):
                result[x] += result[x+1]            
            index += 1
        return result
        