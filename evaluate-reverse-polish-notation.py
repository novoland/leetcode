class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        for x in tokens:
            # print stack
            if x == '+':
                r = stack.pop() + stack.pop()
            elif x == '-':
                a = stack.pop()
                b = stack.pop()                
                r = b - a
            elif x == '*':
                r = stack.pop() * stack.pop()
            elif x == '/':
                a = float(stack.pop())
                b = float(stack.pop())                 
                r = int(b / a)                               
            else:
                r = int(x)            
            stack.append(r)
        return stack.pop()