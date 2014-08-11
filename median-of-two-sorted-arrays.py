class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if not A and not B:
            return
        elif not A:
            size = len(B)
            if size%2 ==0:
                return float((B[size/2-1]+B[size/2]))/2
            else:
                return B[size/2]
        elif not B:
            size = len(A)
            if size%2 ==0:
                return float((A[size/2-1]+A[size/2]))/2
            else:
                return A[size/2]
        sizeA = len(A)
        sizeB = len(B)
        mid = (sizeA+sizeB)/2 + 1
        index,indexA,indexB = 0,0,0
        result = None
        last,cur = None,None

        while index < mid:
            last = cur
            if indexA < sizeA and indexB < sizeB:
                if A[indexA] <= B[indexB]:
                    cur = A[indexA]
                    indexA += 1                    
                else:
                    cur = B[indexB]
                    indexB += 1                    
            elif indexA >= sizeA and indexB < sizeB:
                cur = B[indexB]
                indexB += 1                
            elif indexA < sizeA and indexB >= sizeB:
                cur = A[indexA]
                indexA += 1                
            index += 1

        if (sizeA+sizeB)%2 == 0:
            result = float(last + cur)/2
        else:
            result = cur

        return result