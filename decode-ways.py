class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        result=[0]*(len(s)+1)
        if s[0] == '0':
            return 0
        result[0],result[1]=1,1 
        for x in xrange(2,len(s)+1):
            if s[x-1] != '0':
                result[x] += result[x-1]
            if int(s[x-2:x]) < 27 and int(s[x-2:x]) >9:
                result[x] += result[x-2]
        return result[len(s)]