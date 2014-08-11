class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return
        size = len(digits)
        digits[size-1] +=1
        flag = False
        for x in xrange(size-1,-1,-1):
            if flag:
                digits[x] += 1
            if digits[x] > 9:
                digits[x] = digits[x]%10
                flag = True
            else:
                flag = False
            if flag and x == 0:
                digits.insert(0,1)
                break;
        return digits