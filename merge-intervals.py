class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []
        data = []
        result = []
        for x in intervals:
            data.append(x.start)
            data.append(x.end)    
        a,b=min(data),max(data)
        table=[0]*(b-a+1)
        for x in intervals:
            if x.start == x.end and [x.start,x.end] not in result:
                result.append([x.start,x.end])
                continue
            for y in xrange(x.start,x.end):
                table[y-a]=1
        pre = -1
        flag = False
        # print table
        for x in xrange(0,len(table)):
            if not table[x]:
                if flag:
                    for i in xrange(pre+a,x+a+1):
                        if [i,i] in result:
                            result.remove([i,i])                      
                    result.append([pre+a,x+a])
                    flag = False
                else:
                    pass
            else:
                if not flag:
                    pre = x
                    flag = True
        if flag:
            result.append([pre+a,b])
        return result