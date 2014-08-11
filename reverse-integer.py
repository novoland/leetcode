class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return x
        isNegtive = True if x < 0 else False
        num = abs(x)
        result = 0
        while num:
            n = num % 10 
            num = num / 10
            result = result*10 + n
        if isNegtive:
            result = -result
        return result