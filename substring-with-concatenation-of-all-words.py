class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if not S or not L:
            return []
        table = {}
        for x in L:
            if x not in table:
                table[x] = 1
            else:
                table[x] += 1
        count = len(L)
        sizeword,size = len(L[0]),len(S)
        words = sizeword*count
        result = []
        for x in xrange(size-words+1):
            t = 0
            cur = {}
            for y in xrange(x,x+words,sizeword):
                tmp = S[y:y+sizeword]
                if tmp not in table:
                    break
                if tmp in cur:
                    cur[tmp] += 1
                else:
                    cur[tmp] = 1
                if cur[tmp] > table[tmp]:
                    break
                t += 1
            if t == count:
                result.append(x)
        return result