class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0
        copy = height[:]
        copy.append(0)
        size = len(copy)
        if size == 1:
            return copy[0]
        stack = []
        top = -1
        result = 0
        for x in xrange(size):
            if not stack or copy[stack[top]] <= copy[x]:
                stack.append(x)
                top += 1
            else:                
                while stack and copy[stack[top]] > copy[x]:
                    t = stack.pop();
                    top -= 1;
                    area = copy[t]*(x if not stack else x-stack[top]-1)
                    result = area if area > result else result
                stack.append(x)
                top += 1 
   
        return result