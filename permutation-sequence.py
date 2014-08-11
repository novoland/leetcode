class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if not n or not k:
            return ""
        data = [0]*(n+1)
        data[0] = 1
        for x in xrange(1,n+1):
            data[x]=data[x-1]*x
        if k > data[n]:
            return ""
        index = 1
        path = []
        table = [x for x in xrange(1,n+1)]
        for x in xrange(n-1,-1,-1):
            for y in xrange(1,len(table)+1):
                # print y*data[x]
                # print k
                if y*data[x] == k:
                    path.append(str(table[y-1]))
                    k -= y*data[x]
                    del table[y-1]
                    break
                elif y*data[x] > k:
                    path.append(str(table[y-1]))
                    del table[y-1]
                    k -= (y-1)*data[x]
                    break   
            if not k:
                for i in xrange(len(table)-1,-1,-1):
                    path.append(str(table[i]))
                break
        return "".join(path)