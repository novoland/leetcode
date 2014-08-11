class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if not n or not k:
            return []
        if n < k:
            return []
        data=[]
        for x in xrange(1,n+1):
            data.append(x)
        return self.deal(data, k)

    def deal(self,data,k):
        result = []
        if not data or not k:
            return result
        size = len(data)
        if size < k:
            return result        
        for x in xrange(0,size):
            if k == 1:
                result.append([data[x]])
            else:
                tmp = self.deal(data[x+1:], k-1)
                for y in tmp:
                    y.insert(0,data[x])
                    result.append(y)
        return result