class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return [""]
        stack=[[],[]]
        table = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}        
        cur,pre=0,1
        stack[cur] = map(None,table[digits[0]])
        i,size = 1,len(digits)
        while i < size:
            cur,pre=pre,cur
            stack[cur]=[]
            t = digits[i]
            # print stack[pre]
            if t in table:
                for x in stack[pre]:
                    for y in table[t]:
                        stack[cur].append(x+y)
            # print stack[cur]
            i += 1
        return stack[cur]