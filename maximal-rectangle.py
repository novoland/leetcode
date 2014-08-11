class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0 for x in xrange(col+1)]
        maxarea = 0
        for x in xrange(row):
            stack = []
            top = -1
            for y in xrange(col+1):
                if y < col:
                    if matrix[x][y] == '1':
                        height[y] += 1
                    else:
                        height[y] = 0
                if not stack or height[stack[top]] <= height[y]:
                    stack.append(y)
                    top += 1
                else:
                    while stack and height[stack[top]] > height[y]:
                        t = stack.pop()
                        top -= 1
                        area = height[t] * (y if not stack else y - stack[top] -1)
                        maxarea = area if area > maxarea else maxarea
                    stack.append(y)
                    top += 1
        return maxarea