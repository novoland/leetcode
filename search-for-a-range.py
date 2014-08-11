class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        result = self.search(A, target, 0, len(A)-1)
        if result == -1:
            return [-1,-1]
        start,end,index=result,result,result-1
        while index>=0:
            if A[index]==target:
                start-=1
                index-=1
            else:
                break
        index = result+1
        while index < len(A):
            if A[index] == target:
                end += 1
                index+=1
            else:
                break
        return [start,end]


    def search(self,A,target,start,end):
        if not A:
            return -1
        if start > end:
            return -1
        mid = (end - start)/2+start
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.search(A,target,mid+1,end)
        else:
            return self.search(A,target,start,mid-1)