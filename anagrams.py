class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        if not strs:
            return []
        result = {}
        res = []
        for x in strs:
            t = "".join(sorted(x))
            if t in result:
                if result[t] != None:
                    res.append(result[t])
                    result[t] = None
                res.append(x)
            else:
                result[t] = x
        return res