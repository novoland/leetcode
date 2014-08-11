class Solution:
    def check(self,tmp,t):
        flag = True
        for x in xrange(0,len(tmp)):
            if tmp[x][0] == t[0] or tmp[x][1] == t[1]:
                return False
            r = float(tmp[x][0]-t[0])/(tmp[x][1]-t[1])  
            if r == 1 or r == -1:
                return False
            else :
                x = x + 1            
        return flag
    # @return an integer
    def totalNQueens(self, n):
        if not n:
            return 0
        if n==1:
            return 1
        result = []
        tmp = [[0,0]]
        while tmp:
            last = tmp[len(tmp)-1]
            for x in xrange(0,n):
                t = [x,last[1]+1]
                if self.check(tmp,t):
                    tmp.append(t)
                    if len(tmp) == n:
                        result.append(tmp[:])
                        tmp.pop()
                    else:
                        break
                x = x+1
                if x == n:               
                    while tmp:
                        last = tmp.pop()  
                        flag = False
                        while last[0] + 1 < n:
                            last[0] = last[0] + 1
                            if self.check(tmp,last):
                                tmp.append(last)
                                flag = True
                                break
                        if flag:
                            break
        return len(result)