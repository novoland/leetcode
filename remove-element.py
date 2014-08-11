class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        num,pre,cur,size = 0,0,0,len(A)
        while cur < size:
            if A[cur] == elem:
                cur += 1
                num += 1
                continue
            A[pre] = A[cur]
            pre += 1
            cur += 1
        # print A
        return len(A) - num 