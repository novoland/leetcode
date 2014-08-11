class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if not s:
            return []
        size = len(s)
        stack = []
        for x in xrange(1,4):
            for y in xrange(1,4):
                for z in xrange(1,4):
                    for i in xrange(1,4):
                        if x+y+z+i == size:
                            stack.append([x,y,z,i])
        # print stack
        result = []
        for x in stack:
            data = []
            tmp = s
            for y in x:
                t = tmp[:y]
                if len(t) >1 and t[0] == '0':
                    data=[]
                    break
                if int(t) <256:
                    data.append(t)
                    tmp = tmp[y:]
                else:
                    data = []
                    break
            if data:
                result.append(".".join(data))
        return result