class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        self.stack = []
        self.sum = 0
        self.result = []
        candidates.sort()
        self.deal(candidates,target,0,len(candidates))
        return self.result


    def deal(self,candidates,target,start,end):
        # print self.stack
        # print target
        # print self.sum
        # print '----'
        for x in xrange(start,end):
            self.stack.append(candidates[x])
            self.sum += candidates[x]
            if target == self.sum:
                self.result.append(self.stack[:])
            elif target > self.sum:
                self.deal(candidates,target,x,end)
            self.stack.pop()
            self.sum -= candidates[x]