class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        data = [0 for x in xrange(32)]
        result = 0
        neg = 0
        for x in xrange(32):
            for y in A:
                if y < 0:
                    y = -y
                    neg += 1
                if (y >> x)&1:
                    data[x] += 1
            result |= ((data[x]%3)<<x)

        return result if (neg/32)%3 == 0 else -result