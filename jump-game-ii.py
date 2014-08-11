class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if not A:
            return
        last = 0
        count = 0
        cur = 0
        size = len(A)
        for x in xrange(0,size):
            if x > last:
                if cur == last and last < size -1 :
                    return -1
                last = cur
                count += 1
            cur = cur if cur > A[x] + x else A[x] + x
        return count