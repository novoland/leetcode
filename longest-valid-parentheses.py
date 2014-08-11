class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if not s:
            return 0
        stack=[]
        top = -1
        for x in xrange(len(s)):
            if not stack:
                stack.append(x)
                top += 1
                continue
            if s[x] == ')' and s[stack[top]] == '(':
                stack.pop()
                top -=1
            else:
                stack.append(x)
                top += 1
        # print stack
        size,maxcount = len(s),0
        if not stack:
            return len(s)
        while stack:
            if size-stack[top]-1>maxcount:
                maxcount = size-stack[top]-1
            size = stack.pop()
            top -= 1
            if not stack:
                if size > maxcount:
                    maxcount = size
        return maxcount