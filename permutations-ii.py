class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        result = [num]
        tmp = []
        size = len(num)
        for x in xrange(size):
            for i in result:
                for y in xrange(x+1,size):
                    t =i[:]
                    t[x],t[y]=t[y],t[x]
                    if t not in result and t not in tmp:
                        tmp.append(t)
            result.extend(tmp)
            tmp = []
        return result