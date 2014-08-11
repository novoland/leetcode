class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        result = 0
        if not grid:
            return result
        xsize = len(grid)
        ysize = len(grid[0])
        for x in xrange(0,xsize):
            for y in xrange(0,ysize):
                if x == 0 and y != 0:
                   grid[x][y] += grid[x][y-1]
                elif x != 0 and y == 0:
                    grid[x][y] += grid[x-1][y]
                elif x !=0 and y != 0:
                    grid[x][y] +=  grid[x-1][y] if grid[x-1][y]<grid[x][y-1] else grid[x][y-1]
        return grid[xsize-1][ysize-1]
        