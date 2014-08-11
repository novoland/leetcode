class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s or len(s) == 1:
            return True
        length = len(s)
        start = 0
        end = length - 1
        lowerStr= s.lower()
        char = 'abcdefghijklmnopqrstuvwxyz1234567890'
        while start < end:
            if lowerStr[start] not in char:
                start += 1
                continue
            if lowerStr[end] not in char:
                end -= 1
                continue                
            if lowerStr[start] == lowerStr[end]:
                start += 1
                end -= 1
            else:
                return False
        return True