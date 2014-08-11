class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if not num or len(num) <= 2:
            return 0 
        num.sort()
        size = len(num)
        result,flag = 0,1000000
        for x in xrange(size):
            i = x+1
            j = size-1
            while i<j:
                t = num[x]+num[i]+num[j]
                if abs(t-target)<flag:
                    result = t
                    flag = abs(t-target)
                if t > target:
                    j -= 1
                else:
                    i += 1
        return result