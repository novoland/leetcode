class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        index = 0
        flag = True
        result = []
        while flag:
            m = None
            if index < len(strs[0]):
                m = strs[0][index]
            else:
                break
            for x in xrange(0,len(strs),1):
                if index >= len(strs[x]) or strs[x][index] != m:
                    flag = False
                    break
            if flag:
                result.append(m)
                index += 1
        return "".join(result)