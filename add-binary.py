class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if not a and not b:
            return ''
        strlong = None
        strshort = None
        if len(a) > len(b):
            strlong = a
            strshort = b
        else:
            strlong = b
            strshort = a
        lsize = len(strlong)
        ssize = len(strshort)
        result = []
        flag = 0
        for x in xrange(ssize-1,-1,-1):
            t = int(strshort[x]) + int(strlong[x+lsize-ssize]) + flag
            if t > 1:
                flag = 1
                result.append(str(t-2))
            else:
                flag = 0
                result.append(str(t))
        for x in xrange(lsize-ssize-1,-1,-1):
            t = int(strlong[x]) + flag
            if t > 1:
                flag = 1
                result.append(str(t-2))
            else:
                flag = 0
                result.append(str(t))
        if flag == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)