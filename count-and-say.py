class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <= 0:
            return ""
        a,i = "1",0
        while i < n-1:
            # print a
            pre,count,data = "",0,[]
            for x in a:
                if x == pre:
                    count += 1
                else:
                    if count:
                        data.append(str(count))
                        data.append(pre)
                    pre,count=x,1
            if count:
                data.append(str(count))
                data.append(pre)
            a = "".join(data)
            i += 1
        return a