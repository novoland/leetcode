class Solution:
    def subsetsWithDup(self,S):
        result = []
        if not S:
            return result
        dic = {}
        tmp = []
        tmp1 = []
        for x in S:
            if x not in dic:
                dic[x] = 1
                tmp.append([x])                
            else:
                dic[x] += 1
                t = [x]
                for n in xrange(1,dic[x],1):
                    t.append(x)
                tmp.append(t[:])
        key = dic.keys()  
        result.extend(tmp[:])  
        while True:
            for x in tmp:
                for y in key:
                    if x[len(x)-1] < y:
                        t = x[:]
                        t.append(y)
                        tmp1.append(t)
                        if dic[y] > 1: 
                            t1 = t[:]
                            for z in xrange(1,dic[y],1):
                                t1.append(y)
                                tmp1.append(t1[:])
            if not tmp1:
                break
            result.extend(tmp1[:])            
            tmp = tmp1[:]
            tmp1 = []
        result.append([])
        return result

