class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        s = str(x)
        x = 0
        y = len(s)-1
        while x<y:
            if s[x] != s[y]:
                return False
            else:
                x += 1
                y -= 1
        return True
        