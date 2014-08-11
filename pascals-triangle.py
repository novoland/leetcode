class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows:
            return []
        result = [[1]]
        for x in xrange(1,numRows):
            last = result[x-1]
            tmp = []
            for y in xrange(0,len(last)):
                if y==0:
                    tmp.append(1)
                if y+1 == len(last):
                    tmp.append(1)
                else:
                    tmp.append(last[y]+last[y+1])
                y = y+1
            result.append(tmp)
        return result
        