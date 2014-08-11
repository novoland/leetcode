class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0        
        num,start = 0,0
        while start < len(str) and str[start]==' ':
            start += 1
        end = len(str)-1
        while end >= 1 and str[end]==' ':
            end -= 1
        isnegtive = True if str[start] =='-' else False
        start = start+1 if str[start] =='-' or str[start] =='+' else start
        flag = False
        for x in xrange(start,end+1):
            if str[x] in "0123456789":
                num = num*10 + int(str[x])
            else:
                break
            if num > 2147483647:
                num = 2147483647
                break
            if num == 2147483647:
                flag = True
        if isnegtive:
            if num == 2147483647 and not flag:
                num = -2147483648
            else:
                num = -num
        return num