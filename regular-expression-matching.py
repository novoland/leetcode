class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        sizep,sizes=len(p),len(s)
        dp=[[False for i in range(sizep+1)] for j in range(sizes+1)]
        dp[0][0]=True
        for x in xrange(1,sizep+1):
            if p[x-1] == '*' and x >= 2:
                dp[0][x] = dp[0][x-2]

        for x in xrange(1,sizes+1):
            for y in xrange(1,sizep+1):
                if p[y-1] == '.':
                    dp[x][y] = dp[x-1][y-1]
                elif p[y-1] == '*':
                    dp[x][y] = dp[x][y-2] or dp[x][y-1] or (dp[x-1][y] and (s[x-1]==p[y-2] or p[y-2]=='.'))
                else:
                    dp[x][y] = dp[x-1][y-1] and s[x-1]==p[y-1]
        return dp[sizes][sizep]