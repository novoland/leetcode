class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        size = len(prices)
        if size == 1:
            return 0
        stack = []
        profit = 0
        for x in xrange(0,size):
            flag = None

            if x > 0 and x <size-1:
                if prices[x]>=prices[x-1] and prices[x]>=prices[x+1]:
                    flag = 'high'
                elif prices[x]<=prices[x-1] and prices[x]<=prices[x+1]:
                    flag = 'low'
                else:
                    pass
            elif x == 0:
                if prices[x]>prices[x+1]:
                    flag = 'high'
                elif prices[x]==prices[x+1]:
                    pass
                else:
                    flag = 'low'
            elif x == size-1:
                if prices[x]>prices[x-1]:
                    flag = 'high'
                elif prices[x]==prices[x-1]:
                    pass                    
                else:
                    flag = 'low'
            else:
                pass
            # print prices[x]
            # print flag
            # print stack
            if flag == 'high':
                if stack:
                    top = stack.pop()
                    if top[1]=='high':
                        pass
                    else:
                        profit += prices[x]-top[0]
                else:
                    pass
            elif flag == 'low':
                if stack:
                    top = stack.pop()
                    stack.append([prices[x],'low'])
                else:
                    stack.append([prices[x],'low'])

        return profit