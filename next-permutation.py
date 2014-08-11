class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return []
        size= len(num)-1
        index,i,m=size,size,100000
        while index>0:
            if num[index] > num[index-1]:
                for x in xrange(index,size+1):
                    if num[x] > num[index-1] and num[x] < m:
                        m = num[x]
                        i = x
                num[i],num[index-1]=num[index-1],num[i]
                left = num[:index]
                right = num[index:]
                right.sort()
                left.extend(right)
                return left
            else:
                index -= 1
        num.sort()
        return num