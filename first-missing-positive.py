class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        A.sort()
        pre = 0
        for x in A:
            if x <= 0:
                continue
            if x ==(pre + 1) or x == pre:
                pre = x
            else:
                break
        return pre+1