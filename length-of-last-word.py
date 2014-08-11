class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        result = 0
        s = s.rstrip()
        for x in xrange(len(s)-1,-1,-1):
            if s[x] == ' ':
                break
            else:
                result +=1
        return result
        