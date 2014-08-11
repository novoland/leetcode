class Solution:
    # @return a string
    def convert(self, s, nRows):
        if not s or not nRows:
            return ""
        result = [[] for x in xrange(nRows)]
        index,size = 0,len(s)
        while index < size:
            for x in xrange(nRows):
                if index < size:
                    result[x].append(s[index])
                    index += 1
            for x in xrange(nRows-2,0,-1):
                if index < size:
                    result[x].append(s[index])
                    index += 1                
        s = ""
        for x in result:
            s  += "".join(x)
        return s