class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 1:
            return x
        low,high=0,x        
        while low<=high:
            mid = (low+high)/2.0
            if abs(mid*mid-x) <0.00001:
                return int(mid)
            elif mid*mid > x:
                high = mid
            else:
                low = mid