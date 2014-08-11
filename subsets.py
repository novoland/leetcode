class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = []
        flag = True
        if S:
            for x in S:
                result.append([x])
            size = len(result)
            row = result[:]
            row2 = []
            while row:
                for x in row:
                    for y in S:
                        if y > x[len(x)-1]:
                            t = x[:]
                            t.append(y)
                            row2.append(t)                    
                row = row2[:]
                result.extend(row)
                row2 = []  
        result.append([])
        return result