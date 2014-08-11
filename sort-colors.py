class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return
        table = {0:0,1:0,2:0}
        for x in A:
            if x in table:
                table[x] += 1
        for x in xrange(0,table[0]):
            A[x] = 0
        for x in xrange(table[0],table[0]+table[1]):
            A[x] = 1   
        for x in xrange(table[0]+table[1],table[0]+table[1]+table[2]):
            A[x] = 2                      