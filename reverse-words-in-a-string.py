class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s or not s.strip():
            return ""
        a = self.reverse(list(s))
        t = a.lstrip(" ").rstrip(" ").split(" ")
        result = ""
        for x in t:
            if x:
                result +=self.reverse(list(x))+" "        
        return result[:len(result)-1]

    def reverse(self,s):
        first = 0
        last = len(s) - 1
        while first <= last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp
            first += 1
            last -= 1
        return "".join(s)