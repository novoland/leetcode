class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n > 0:
            a,b = n>>1,n%2
            c = self.pow(x,a)
            return c*c*x if b == 1 else c*c
        else:
            return 1.0/self.pow(x,-n)