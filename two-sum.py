class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if not num:
            return ()
        data = sorted(num)
        low,high=0,len(data)-1
        while low < high:
            tmp = data[low]+data[high]
            if tmp == target:
                if data[low] == data[high]:
                    a = num.index(data[low])+1
                    b = num[a:].index(data[high])+a+1
                    return (a,b)
                else:
                    a = num.index(data[low])+1
                    b = num.index(data[high])+1
                    return (min(a,b),max(a,b))
            elif tmp < target:
                low += 1
            else:
                high -= 1
        return ()