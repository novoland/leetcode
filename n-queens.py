class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.n = n
        self.stack = []
        self.stackTop = -1
        self.result = []
        self.explore()
        return self.result

    def explore(self):
        if self.stackTop == self.n - 1:
            self.setResult()
            return
        for x in xrange(0,self.n):            
            self.stackTop += 1
            self.stack.append(x)
            if self.check():
                self.explore()

            self.stack.pop()
            self.stackTop -= 1
            


    def check(self):
        last = self.stack[self.stackTop]
        i = self.stackTop - 1
        while i >= 0:
            col = self.stack[i]
            if col == last or abs( last- col) == abs(self.stackTop - i):
                return False
            i -= 1
        return True

    def setResult(self):
        tmp = [['.']*self.n for x in range(self.n)]
        t= []
        for x in range(0,self.stackTop+1,1):
            tmp[x][self.stack[x]] = 'Q'
        for x in xrange(0,self.n,1):
            t.append(''.join(tmp[x]))
        self.result.append(t)