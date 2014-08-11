class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1 and word2:
            return len(word2)
        if word1 and not word2:
            return len(word1)
        size1 = len(word1)+1
        size2 = len(word2)+1
        result = [[None]*size1 for x in range(size2)]
        for x in range(0,size1):
            result[0][x] = x
        for x in range(0,size2):
            result[x][0] = x       
        for x in range(1,size2):
            for y in range(1,size1):
                if word1[y-1] == word2[x-1]:
                    result[x][y] = result[x-1][y-1]
                else:
                    result[x][y]=self.minNum(result[x-1][y],result[x][y-1],result[x-1][y-1])+1
        return result[size2-1][size1-1]

    def minNum(self,a,b,c):
        minN = b if a > b else a
        return  minN if c > minN else c