class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if not n:
            return []
        lc,rc = 1,0
        stack = [['(',1,0]]
        while stack and len(stack[0][0]) != 2*n:
            tmp = []
            # print stack
            for x in stack:
                for y in "()":
                    t = x[0]                    
                    if y == '(' and x[1] < n:
                        t += y
                        tmp.append([t,x[1]+1,x[2]])
                    elif y == ')' and x[1] > x[2] and x[2] < n:
                        t += y
                        tmp.append([t,x[1],x[2]+1])
                        
            stack = tmp
        result = []
        for x in stack:
            result.append(x[0])
        return result