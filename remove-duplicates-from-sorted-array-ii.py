class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        count = 1
        delete = [False]
        pre = A[0]
        for x in xrange(1,len(A)):
            if A[x] == pre:
                count += 1
                if count > 2:
                    delete.append(True)
                else:
                    delete.append(False)
            else:
                count = 1
                pre = A[x]
                delete.append(False)
        index = 0
        # print delete
        for x in xrange(0,len(delete)):
            if not delete[x]:
                A[index] = A[x]
                index += 1
        # print A
        return index