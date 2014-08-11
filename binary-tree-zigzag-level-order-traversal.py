class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = [[root.val]]
        row = [root]
        tmp = []
        value = []
        index = 1
        while row:
            t = row[0]
            if t.left:
                tmp.append(t.left)
                value.append(t.left.val)
            if t.right:
                tmp.append(t.right)
                value.append(t.right.val)
            del row[0]
            if not row and tmp:
                index += 1
                row = tmp[:]
                if index%2 != 0:
                    result.append(value[:])
                else:
                    value.reverse()
                    result.append(value[:])
                tmp = []
                value = []
        return result