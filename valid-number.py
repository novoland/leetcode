class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if not s:
            return False
        start,end=0,len(s)-1
        while start<=end and s[start] == ' ':
            start += 1
        while end >=start and s[end] == ' ':
            end -= 1
        if start > end:
            return False
        count1,count2=0,0
        if s[start] == '+' or s[start] == '-':
            start += 1
        for x in xrange(start,end+1):
            if s[x] not in "0123456789.eE+-":
                return False
            if s[x] in "eE":
                count1 += 1
                if count1 > 1:
                    return False
                if x-1<start or x+1 > end:
                    return False     
                if x==start+1 and s[start]=='.':
                    return False
            if s[x] == '.':
                count2 += 1
                if count2 > 1 or count1 >= 1:
                    return False
                if x-1<start and x+1 > end:
                    return False    
                if x-1>=start and s[x-1]=='e':
                    return False    
            if s[x] in '+-':
                if x-1<start or x+1 > end:
                    return False 
                if x-1>=start and s[x-1]!='e':
                    return False                            
                    
        return True