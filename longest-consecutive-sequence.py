class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        self.result = {}
        self.tmp = {}
        self.max = 0
        for x in num:
            self.check(x)
        return self.max

    def  check(self,target):
        if target in self.tmp:
            return
        else:
            self.tmp[target] = target
        if target+1 in self.result and target-1 in self.result:
            low = self.result[target-1]
            high = self.result[target+1]
            del self.result[target-1]
            del self.result[target+1]            
            self.result[low] = high
            self.result[high] = low
            if abs(high - low)+1 > self.max:
                self.max = abs(high - low)+1            
        elif target+1 in self.result:
            high = self.result[target+1]
            del self.result[target+1] 
            self.result[target] = high
            self.result[high] = target      
            if abs(high - target)+1 > self.max:
                self.max = abs(high - target)+1
        elif target-1 in self.result:
            low = self.result[target-1]                       
            del self.result[target-1]
            self.result[target] = low 
            self.result[low] = target
            if abs(low - target)+1 > self.max:
                self.max = abs(low - target)+1   
        else:   
            self.result[target] = target
            if self.max < 1:
                self.max = 1