class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if not num2 or not num1:
            return ""
        if num1=="0" or num2 == "0":
            return "0"
        size1,size2 = len(num1),len(num2)
        cur = num1 if size1 > size2 else num2
        table = {"0":"0","1":cur}
        result = cur        
        for x in xrange(2,10):
            result=self.add(result,cur)
            table[str(x)] = result
        result = ""
        i = 0
        cur = num2 if size1 > size2 else num1
        size = min(size1,size2)
        for x in xrange(size-1,-1,-1):
            t = table[cur[x]]+"0"*(size-x-1)
            result = self.add(result,t)
        return result

    def add(self,num1,num2):
        if not num1:
            return num2
        if not num2:
            return num1
        size1,size2 = len(num1),len(num2)
        carry = 0
        data = []
        i = 0
        str1,str2=num1[::-1],num2[::-1]
        for x in xrange(0,max(size1,size2)):
            a = carry
            a += int(str1[x]) if x < size1 else 0
            a += int(str2[x]) if x < size2 else 0
            if a < 10:
                data.append(str(a))
                carry = 0
            else:
                data.append(str(a%10))
                carry = 1
            i += 1
        if carry:
            data.append("1")
        data.reverse()
        return "".join(data)