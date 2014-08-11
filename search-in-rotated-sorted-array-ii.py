class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if not A:
            return False
        size = len(A)
        if target == A[0]:
            return True
        elif target > A[0]:
            index = 1
            while index < size:
                if target == A[index]:
                    return True
                if index < size-1 and A[index]>A[index+1]:
                    break
                index += 1
        else:
            index = size-1
            while index >=0:
                if target == A[index]:
                    return True
                if index >0 and A[index]<A[index-1]:
                    break
                index -= 1
        return False
        