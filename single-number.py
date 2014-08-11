class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        s = 0
        for a in A:
            s ^= a
        return s
        