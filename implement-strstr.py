class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if haystack == None or needle == None:
            return 
        haystackLen = len(haystack)
        needleLen = len(needle)
        if needleLen > haystackLen:
            return
        elif needleLen == 0:
            return haystack
        hi,ni,i,last=0,0,0,0
        count = 1
        for x in xrange(1,needleLen):
            if needle[x] == needle[0]:
                count = x
                break
        while hi < haystackLen:
            if haystack[hi] == needle[ni]:
                hi += 1
                ni += 1
                i += 1
            else:
                if i == 0:
                    last += 1
                else:
                    if i > count:
                        last += count
                    else:
                        last += i
                ni = 0
                hi = last
                i = 0
            if ni == needleLen:
                return haystack[last:]
        return