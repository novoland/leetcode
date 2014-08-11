class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if not num:
            return []
        num.sort()
        size = len(num)
        stack = []
        for x in xrange(size):
            if x == 0 or num[x] > num[x-1]:
                low=x+1;high=size-1
                while low < high:
                    t = num[low]+num[high]
                    if t == -num[x]:
                        stack.append([num[x],num[low],num[high]])
                        low += 1
                        high -= 1
                        while low < high and num[low-1] == num[low]:low += 1
                        while low < high and num[high+1] == num[high]:high -= 1
                    elif t > -num[x]:
                        while low < high:
                            high -= 1
                            if num[high] < num[high+1]:break                            
                    elif t < -num[x]:
                        while low < high:
                            low += 1
                            if num[low-1] < num[low]:break                     
        return stack