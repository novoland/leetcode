class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
        stack1 = list(s)
        stack2 = []
        while stack1:
            tmp = stack1.pop() 
            if not stack2:
                stack2.append(tmp)
                continue
            else:
                if self.f(tmp,stack2[-1]):
                    stack2.pop()
                else:
                    stack2.append(tmp)
        if not stack1 and not stack2:
            return True
        else:
            return False

    def f(self,a,b):
        if a == '[' and b ==']':
            return True
        elif a == '(' and b ==')':
            return True
        elif a == '{' and b =='}':
            return True
        else:
            return False