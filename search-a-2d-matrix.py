class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        for x in xrange(0,len(matrix),1):
            if matrix[x][0] == target:
                return True
            elif matrix[x][0] >target:
                if x == 0:
                    return False
                else:
                    return self.searchRow(matrix[x-1],target)
        return self.searchRow(matrix[len(matrix)-1],target)

    def searchRow(self,row,target):
        if not row:
            return False
        return self.search(0,len(row)-1,row,target)

    def search(self,start,end,row,target):
        if start > end:
            return False
        mid = (start+end)/2
        if row[mid] == target:
            return True
        elif row[mid]  > target:
            return self.search(start,mid-1,row,target)
        elif row[mid]  < target:
            return self.search(mid+1,end,row,target)
        