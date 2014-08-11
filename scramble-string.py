class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True        
        size = len(s1)
        for x in xrange(size-1):
            a = sorted(s1[:x+1])
            b = sorted(s2[:x+1])
            c = sorted(s2[size-x-1:])
            # print a
            # print b
            # print c
            if a == b:
                flag = self.isScramble(s1[x+1:],s2[x+1:]) and self.isScramble(s1[:x+1],s2[:x+1])
                if flag:
                    return flag
                else:
                    continue
            elif a == c:
                flag= self.isScramble(s1[x+1:],s2[:size-x-1]) and self.isScramble(s1[:x+1],s2[size-x-1:])
                if flag:
                    return flag
                else:
                    continue                
        return False