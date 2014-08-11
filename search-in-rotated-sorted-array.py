class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1
        size = len(A)
        if A[0] == target:
            return 0
        elif A[0] > target:            
            index = size-1
            last = A[index]+1
            while index > -1 and last > A[index]:
                if A[index] == target:
                    return index
                elif A[index] > target:
                    last = A[index]
                    index -= 1
                else:
                    return -1
        else:
            index = 0
            last = A[index]-1
            while index < size and last < A[index]:
                if A[index] == target:
                    return index
                elif A[index] < target:
                    last = A[index]
                    index += 1
                else:
                    return -1    
        return -1