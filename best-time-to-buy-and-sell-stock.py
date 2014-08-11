class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        minp = prices[0]
        maxp = prices[0]
        profit = 0
        for x in prices:
            if x < minp:
                profit = maxp-minp if maxp-minp > profit else profit
                minp = x
                maxp = x
            if x > maxp:
                maxp = x
        profit = maxp-minp if maxp-minp > profit else profit
        return profit