class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if not A or not B:
            return
        index = m + n -1
        indexa = m-1
        indexb = n - 1
        while indexa>=0 and indexb>=0:
            if A[indexa] >= B[indexb]:
                A[index] = A[indexa]
                indexa = indexa -1
            else:
                A[index] = B[indexb]
                indexb = indexb -1
            index = index -1
        while indexa>=0:
            A[index] = A[indexa]
            indexa = indexa -1
            index = index -1
        while indexb>=0:
            A[index] = B[indexb]
            indexb = indexb -1
            index = index -1            
        