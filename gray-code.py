class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = [0]
        if not n:
            return result
        if n == 1:
            result.append(1)
            return result
        tmp = self.grayCode(n-1)
        result = tmp
        for x in xrange(len(tmp)-1,-1,-1):
            result.append(1<<n-1^tmp[x])
        return result