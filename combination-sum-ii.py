class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        self.stack = []
        self.result = []
        self.count = 0
        self.deal(candidates,0,len(candidates),target)
        return self.result

    def  deal(self,candidates,start,end,target):
        for x in xrange(start,end):
            self.stack.append(candidates[x])
            self.count += candidates[x]
            if self.count == target:
                if self.stack not in self.result:
                    self.result.append(self.stack[:])
                else:
                    pass
            elif self.count < target:
                self.deal(candidates,x+1,end,target)
            else:
                t = self.stack.pop()
                self.count -= t
                break            
            t = self.stack.pop()
            self.count -= t