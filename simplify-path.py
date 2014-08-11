class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = path.split('/')
        stack.reverse()
        result = []
        # print stack
        while stack:
            # print result
            node = stack.pop()
            if not node or node == '.':
                continue
            if node == '..':
                if len(result) > 0:
                    result.pop()
                    result.pop()
                    continue
                else:
                    continue
            result.append('/')
            result.append(node)

        if len(result) == 0:
            result.append('/')

        return "".join(result)