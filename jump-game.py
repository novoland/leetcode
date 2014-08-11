class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if not A:
            return True
        canReach = 0
        index = 0
        size = len(A)
        while index < size and index <= canReach:
            if index + A[index] > canReach:
                canReach = index + A[index]
            if canReach >= size - 1:
                return True
            index += 1
        return canReach >= size - 1