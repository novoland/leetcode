# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.build(nodes[:i]):
                for right in self.build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
    def generateTrees(self, n):
        nodes = map(TreeNode, range(1, n + 1))
        return map(copy.deepcopy, self.build(nodes))